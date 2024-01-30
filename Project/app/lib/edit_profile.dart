import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class editprofile extends StatefulWidget {
  const editprofile({super.key});

  @override
  State<editprofile> createState() => editprofileState();
}

class editprofileState extends State<editprofile> {
  TextEditingController _nameController = TextEditingController();
  TextEditingController _emailController = TextEditingController();
  TextEditingController _contactController = TextEditingController();
  TextEditingController _addressController = TextEditingController();

  @override
  void initState() {
    super.initState();
    getData();
  }

  Future<void> getData() async {
    final user = FirebaseAuth.instance.currentUser;
    final userId = user?.uid;
    QuerySnapshot<Map<String, dynamic>> querySnapshot = await FirebaseFirestore
        .instance
        .collection('tbl_studentregister')
        .where('Student_id', isEqualTo: userId)
        .limit(1)
        .get();
    if (querySnapshot.docs.isNotEmpty) {
      setState(() {
        _nameController = querySnapshot.docs.first['Student_name'];
        _emailController = querySnapshot.docs.first['Student_email'];
        _contactController = querySnapshot.docs.first['Student_contact'];
        _addressController = querySnapshot.docs.first['Student_address'];
      });
    } else {
      setState(() {
        _nameController = 'Error Loading Data' as TextEditingController;
        _emailController = 'Error Loading Data' as TextEditingController;
        _contactController = 'Error Loading Data' as TextEditingController;
        _addressController = 'Error Loading Data' as TextEditingController;
      });
    }
  }

  void editprofile() {
    print(_nameController.text);
    print(_emailController.text);
    print(_contactController.text);
    print(_addressController.text);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            Text('User editprofile'),
            TextFormField(
              controller: _nameController,
              decoration: InputDecoration(hintText: 'Enter Name'),
            ),
            TextFormField(
              controller: _emailController,
              decoration: InputDecoration(hintText: 'Enter Email'),
            ),
            TextFormField(
              controller: _contactController,
              decoration: InputDecoration(hintText: 'Enter Contact'),
            ),
            TextFormField(
              controller: _addressController,
              decoration: InputDecoration(hintText: 'Enter Address'),
            ),
            ElevatedButton(
                onPressed: () {
                  editprofile();
                },
                child: Text('Save'))
          ],
        ),
      ),
    );
  }
}
