import 'dart:io';
import 'package:edupulse/login.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:file_picker/file_picker.dart';
import 'package:progress_dialog_null_safe/progress_dialog_null_safe.dart';

class Registration extends StatefulWidget {
  const Registration({Key? key}) : super(key: key);

  @override
  State<Registration> createState() => RegistrationState();
}

class RegistrationState extends State<Registration> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _contactController = TextEditingController();
  final TextEditingController _addressController = TextEditingController();
  final TextEditingController _adminoController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  XFile? _selectedImage;
  String? _imageUrl;
  String? _selectedDept;
  String? _selectedCourse;
  String? _selectedYear;
  List<Map<String, dynamic>> deptList = [];
  List<Map<String, dynamic>> courseList = [];
  List<Map<String, dynamic>> yearList = [];
  String? filePath;
  late ProgressDialog _progressDialog;
  @override
  void initState() {
    super.initState();
    _progressDialog = ProgressDialog(context);
    // Call a function to fetch district data when the widget is created
    fetchDeptData();
  }

  Future<void> _pickFile() async {
    try {
      FilePickerResult? result = await FilePicker.platform.pickFiles();

      if (result != null) {
        setState(() {
          filePath = result.files.single.path;
        });
      } else {
        // User canceled file picking
        print('File picking canceled.');
      }
    } catch (e) {
      // Handle exceptions
      print('Error picking file: $e');
    }
  }

  Future<void> _pickImage() async {
    final pickedFile =
        await ImagePicker().pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _selectedImage = XFile(pickedFile.path);
      });
    }
  }

  Future<void> register() async {
    // Implement your registration logic here
    print('Name: ${_nameController.text}');
    print('Email: ${_emailController.text}');
    print('Contact: ${_contactController.text}');
    print('Address: ${_addressController.text}');
    print('Admission Number: ${_adminoController.text}');
    print('Password: ${_passwordController.text}');
    print('Gender: ${selectedGender}');
    print('Department: ${_selectedDept}');
    print('Course: ${_selectedCourse}');
    print('Year: ${_selectedYear}');
    try {
      _progressDialog.show();
      UserCredential userCredential =
          await FirebaseAuth.instance.createUserWithEmailAndPassword(
        email: _emailController.text,
        password: _passwordController.text,
      );

      if (userCredential != null) {
        await _storeUserData(userCredential.user!.uid);
        Fluttertoast.showToast(
          msg: "Registration Successful",
          toastLength: Toast.LENGTH_SHORT,
          gravity: ToastGravity.BOTTOM,
          backgroundColor: Colors.green,
          textColor: Colors.white,
        );
        _progressDialog.hide();
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => Login()),
        );
      }
    } catch (e) {
      _progressDialog.hide();
      Fluttertoast.showToast(
        msg: "Registration Failed",
        toastLength: Toast.LENGTH_SHORT,
        gravity: ToastGravity.BOTTOM,
        backgroundColor: Colors.red,
        textColor: Colors.white,
      );
      print("Error registering user: $e");
      // Handle error, show message, or take appropriate action
    }
  }

  Future<void> _storeUserData(String userId) async {
    try {
      final FirebaseFirestore firestore = FirebaseFirestore.instance;
      await firestore.collection('tbl_studentregister').doc(userId).set({
        'Student_name': _nameController.text,
        'Student_email': _emailController.text,
        'Student_contact': _contactController.text,
        'Student_gender': selectedGender,
        'Student_address': _addressController.text,
        'Student_password': _passwordController.text,
        'course_id': _selectedCourse,
        'year_id': _selectedYear,
        'Student_id': userId,
        'student_status': 0,
        // Add more fields as needed
      });

      await _uploadImage(userId);
    } catch (e) {
      print("Error storing user data: $e");
      // Handle error, show message or take appropriate action
    }
  }

  Future<void> _uploadImage(String userId) async {
    try {
      if (_selectedImage != null) {
        Reference ref =
            FirebaseStorage.instance.ref().child('Student_Photo/$userId.jpg');
        UploadTask uploadTask = ref.putFile(File(_selectedImage!.path));
        TaskSnapshot taskSnapshot = await uploadTask.whenComplete(() => null);

        String imageUrl = await taskSnapshot.ref.getDownloadURL();

        await FirebaseFirestore.instance
            .collection('tbl_studentregister')
            .doc(userId)
            .update({
          'Student_photo': imageUrl,
        });
      }

      if (filePath != null) {
        //FileUpload
        // Step 1: Get the file name from the path
        String fileName = filePath!.split('/').last;

        // Step 2: Upload file to Firebase Storage with the original file name
        Reference fileRef = FirebaseStorage.instance
            .ref()
            .child('Student_Files/$userId/$fileName');
        UploadTask fileUploadTask = fileRef.putFile(File(filePath!));
        TaskSnapshot fileTaskSnapshot =
            await fileUploadTask.whenComplete(() => null);

        // Step 3: Get download URL of the uploaded file
        String fileUrl = await fileTaskSnapshot.ref.getDownloadURL();

        // Step 4: Update user's collection in Firestore with the file URL
        await FirebaseFirestore.instance
            .collection('tbl_studentregister')
            .doc(userId)
            .update({
          'Student_file': fileUrl,
        });
      }
    } catch (e) {
      print("Error uploading image: $e");
      // Handle error, show message or take appropriate action
    }
  }

  Future<void> fetchDeptData() async {
    try {
      QuerySnapshot<Map<String, dynamic>> querySnapshot =
          await FirebaseFirestore.instance.collection('tbl_department').get();

      List<Map<String, dynamic>> dept = querySnapshot.docs
          .map((doc) => {
                'id': doc.id,
                'name': doc['department_name'].toString(),
              })
          .toList();

      setState(() {
        deptList = dept;
      });
    } catch (e) {
      print('Error fetching department data: $e');
    }
    try {
      QuerySnapshot<Map<String, dynamic>> querySnapshot =
          await FirebaseFirestore.instance.collection('tbl_year').get();

      List<Map<String, dynamic>> year = querySnapshot.docs
          .map((doc) => {
                'id': doc.id,
                'name': doc['year_name'].toString(),
              })
          .toList();

      setState(() {
        yearList = year;
      });
    } catch (e) {
      print('Error fetching year data: $e');
    }
  }

  Future<void> fetchCourseData(id) async {
    try {
      print(id);
      // Replace 'tbl_course' with your actual collection name
      QuerySnapshot<Map<String, dynamic>> querySnapshot1 =
          await FirebaseFirestore.instance
              .collection('tbl_course')
              .where('department_id', isEqualTo: id)
              .get();

      List<Map<String, dynamic>> dept1 = querySnapshot1.docs
          .map((doc) => {
                'id': doc.id,
                'name': doc['course_name'].toString(),
              })
          .toList();

      setState(() {
        courseList = dept1;
      });
    } catch (e) {
      print('Error fetching course data: $e');
    }
  }

  List<String> courses = ['BCA', 'BBA', 'B.Com'];
  String? selectedCourse;

  List<String> years = ['2021-2024', '2022-2025', '2023-2026'];
  String? selectedYear;

  String? selectedGender;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('EduPulse'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 20),
              Center(
                child: GestureDetector(
                  onTap: _pickImage,
                  child: Stack(
                    children: [
                      CircleAvatar(
                        radius: 50,
                        backgroundColor: const Color(0xff4c505b),
                        backgroundImage: _selectedImage != null
                            ? FileImage(File(_selectedImage!.path))
                            : _imageUrl != null
                                ? NetworkImage(_imageUrl!)
                                : const AssetImage('assets/dummy450x450.jpg')
                                    as ImageProvider,
                        child: _selectedImage == null && _imageUrl == null
                            ? const Icon(
                                Icons.add,
                                size: 40,
                                color: Color.fromARGB(255, 41, 39, 39),
                              )
                            : null,
                      ),
                      if (_selectedImage != null || _imageUrl != null)
                        const Positioned(
                          bottom: 0,
                          right: 0,
                          child: CircleAvatar(
                            backgroundColor: Colors.white,
                            radius: 18,
                            child: Icon(
                              Icons.edit,
                              size: 18,
                              color: Colors.black,
                            ),
                          ),
                        ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 25),
              _buildIconTextField(Icons.person, _nameController, 'Name'),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.email, _emailController, 'Email'),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.phone, _contactController, 'Contact'),
              const SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text(
                    'Gender: ',
                    style: TextStyle(fontWeight: FontWeight.w500, fontSize: 17),
                  ),
                  Row(
                    children: [
                      Radio<String>(
                        activeColor: Colors.blue,
                        value: 'Male',
                        groupValue: selectedGender,
                        onChanged: (value) {
                          setState(() {
                            selectedGender = value!;
                          });
                        },
                      ),
                      const Text('Male')
                    ],
                  ),
                  Row(
                    children: [
                      Radio<String>(
                        activeColor: Colors.blue,
                        value: 'Female',
                        groupValue: selectedGender,
                        onChanged: (value) {
                          setState(() {
                            selectedGender = value!;
                          });
                        },
                      ),
                      const Text('Female')
                    ],
                  ),
                  Row(
                    children: [
                      Radio<String>(
                        activeColor: Colors.blue,
                        value: 'Others',
                        groupValue: selectedGender,
                        onChanged: (value) {
                          setState(() {
                            selectedGender = value!;
                          });
                        },
                      ),
                      const Text('Others')
                    ],
                  ),
                ],
              ),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.home, _addressController, 'Address',
                  multiline: true),
              const SizedBox(height: 10),
              DropdownButtonFormField<String>(
                value: _selectedDept,
                decoration: InputDecoration(
                  prefixIcon: const Icon(Icons.school),
                  hintText: 'Select Department',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                    borderSide: const BorderSide(
                      color: Colors.blue,
                    ), // Adjust color as needed
                  ),
                ),
                onChanged: (String? newValue) {
                  fetchCourseData(newValue);
                  setState(() {
                    _selectedDept = newValue;
                  });
                },
                isExpanded: true,
                items: deptList.map<DropdownMenuItem<String>>(
                  (Map<String, dynamic> department) {
                    return DropdownMenuItem<String>(
                      value: department['id'], // Use document ID as the value
                      child: Text(department['name']),
                    );
                  },
                ).toList(),
              ),
              const SizedBox(height: 10),
              DropdownButtonFormField<String>(
                value: _selectedCourse,
                decoration: InputDecoration(
                  prefixIcon: const Icon(Icons.school),
                  hintText: "Select Course",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                    borderSide: const BorderSide(
                      color: Colors.blue,
                    ), // Adjust color as needed
                  ),
                ),
                onChanged: (String? newValue) {
                  setState(() {
                    _selectedCourse = newValue;
                  });
                },
                isExpanded: true,
                items: courseList.map<DropdownMenuItem<String>>(
                  (Map<String, dynamic> course) {
                    return DropdownMenuItem<String>(
                      value: course['id'], // Use document ID as the value
                      child: Text(course['name']),
                    );
                  },
                ).toList(),
              ),
              const SizedBox(height: 10),
              DropdownButtonFormField<String>(
                value: _selectedYear,
                decoration: InputDecoration(
                  prefixIcon: const Icon(Icons.school),
                  hintText: "Select Year",
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                    borderSide: const BorderSide(
                      color: Colors.blue,
                    ), // Adjust color as needed
                  ),
                ),
                onChanged: (String? newValue) {
                  setState(() {
                    _selectedYear = newValue;
                  });
                },
                isExpanded: true,
                items: yearList.map<DropdownMenuItem<String>>(
                  (Map<String, dynamic> year) {
                    return DropdownMenuItem<String>(
                      value: year['id'], // Use document ID as the value
                      child: Text(year['name']),
                    );
                  },
                ).toList(),
              ),
              const SizedBox(height: 10),
              // _buildIconDropdownField(
              //     Icons.school, selectedCourse, 'Select Course', courses,
              //     (String? newValue) {
              //   setState(() {
              //     selectedCourse = newValue;
              //   });
              // }),
              _buildIconTextField(
                  Icons.school, _adminoController, 'Admission Number'),
              const SizedBox(height: 10),
              Column(
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: ElevatedButton(
                          onPressed: _pickFile,
                          child: Text('Upload File'),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(height: 16),
                  if (filePath != null)
                    Text(
                      'Selected File: $filePath',
                      style: TextStyle(fontSize: 16),
                    ),
                ],
              ),
              const SizedBox(height: 10),
              _buildIconTextField(
                  Icons.security, _passwordController, 'Password',
                  obscureText: true),
              const SizedBox(height: 30),
              ElevatedButton(
                onPressed: register,
                child: const Text('Register'),
                style: ElevatedButton.styleFrom(
                  primary: Colors.deepPurple, // Button color
                  onPrimary: Colors.white, // Text color
                  shape: RoundedRectangleBorder(
                    borderRadius:
                        BorderRadius.circular(10.0), // Rounded corners
                  ),
                  padding: const EdgeInsets.symmetric(
                      vertical: 16.0), // Set vertical padding
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildIconTextField(
      IconData icon, TextEditingController controller, String labelText,
      {bool obscureText = false, bool multiline = false}) {
    return TextFormField(
      maxLines: multiline ? null : 1,
      keyboardType: multiline ? TextInputType.multiline : TextInputType.text,
      controller: controller,
      obscureText: obscureText,
      decoration: InputDecoration(
        labelText: labelText,
        prefixIcon: Icon(icon),
        border: const OutlineInputBorder(),
      ),
    );
  }

  Widget _buildIconDropdownField(IconData icon, String? value, String hintText,
      List<String> items, void Function(String?) onChanged) {
    return DropdownButtonFormField<String>(
      value: value,
      decoration: InputDecoration(
        hintText: hintText,
        prefixIcon: Icon(icon),
        border: const OutlineInputBorder(),
      ),
      onChanged: onChanged,
      items: items.map<DropdownMenuItem<String>>((String item) {
        return DropdownMenuItem<String>(
          value: item,
          child: Text(item),
        );
      }).toList(),
    );
  }
}

void main() {
  runApp(const MaterialApp(
    home: Registration(),
  ));
}
