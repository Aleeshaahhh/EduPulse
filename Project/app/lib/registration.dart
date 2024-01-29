import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/material.dart';

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
  Future<void> _pickImage() async {
    final pickedFile =
        await ImagePicker().pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _selectedImage = XFile(pickedFile.path);
      });
    }
  }

  void register() {
    // Implement your registration logic here
    print('Name: ${_nameController.text}');
    print('Email: ${_emailController.text}');
    print('Contact: ${_contactController.text}');
    print('Address: ${_addressController.text}');
    print('Admission Number: ${_adminoController.text}');
    print('Password: ${_passwordController.text}');
  }

  List<String> departments = ['Dept. of CS', 'Dept. of Management', 'Dept. of Commerce'];
  String? selectedDepartment;

  List<String> courses = ['BCA', 'BBA', 'B.Com'];
  String? selectedCourse;

  List<String> years = ['2021-2024', '2022-2025', '2023-2026'];
  String? selectedYear;

String? selectedGender;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('EduPulse'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Center(
                child: Text(
                  'REGISTER HERE!',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 35, color: Colors.deepPurpleAccent),
                ),
              ),
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
              Row(children: [Text('Gender'),
              Radio<String>(
                      activeColor: Colors.blue,
                      value: 'Male',
                      groupValue: selectedGender,
                      onChanged: (value) {
                        setState(() {
                          selectedGender = value!;
                        });
                      },
                    ),],),
              _buildIconTextField(Icons.home, _addressController, 'Address'),
              const SizedBox(height: 10),
              _buildIconDropdownField(Icons.school, selectedDepartment, 'Select Department', departments, (String? newValue) {
                setState(() {
                  selectedDepartment = newValue;
                });
              }),
              const SizedBox(height: 10),
              _buildIconDropdownField(Icons.school, selectedCourse, 'Select Course', courses, (String? newValue) {
                setState(() {
                  selectedCourse = newValue;
                });
              }),
              const SizedBox(height: 10),
              _buildIconDropdownField(Icons.school, selectedYear, 'Select Year', years, (String? newValue) {
                setState(() {
                  selectedYear = newValue;
                });
              }),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.school, _adminoController, 'Admission Number'),
              const SizedBox(height: 10),
              _buildIconTextField(Icons.security, _passwordController, 'Password', obscureText: true),
              const SizedBox(height: 30),
              ElevatedButton(
                onPressed: register,
                child: Text('Register'),
                style: ElevatedButton.styleFrom(
                  primary: Colors.deepPurple, // Button color
                  onPrimary: Colors.white, // Text color
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0), // Rounded corners
                  ),
                  padding: EdgeInsets.symmetric(vertical: 16.0), // Set vertical padding
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildIconTextField(IconData icon, TextEditingController controller, String labelText, {bool obscureText = false}) {
    return TextFormField(
      controller: controller,
      obscureText: obscureText,
      decoration: InputDecoration(
        labelText: labelText,
        prefixIcon: Icon(icon),
        border: OutlineInputBorder(),
      ),
    );
  }

  Widget _buildIconDropdownField(IconData icon, String? value, String hintText, List<String> items, void Function(String?) onChanged) {
    return DropdownButtonFormField<String>(
      value: value,
      decoration: InputDecoration(
        hintText: hintText,
        prefixIcon: Icon(icon),
        border: OutlineInputBorder(),
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
  runApp(MaterialApp(
    home: Registration(),
  ));
}
