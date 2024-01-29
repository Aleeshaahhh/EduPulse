import 'package:flutter/material.dart';

class editprofile extends StatefulWidget {
  const editprofile({super.key});

  @override
   State<editprofile> createState() =>editprofileState();
}
class editprofileState extends State<editprofile> {
  final TextEditingController _nameController = TextEditingController(); 
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _contactController = TextEditingController();
  final TextEditingController _addressController = TextEditingController();
  void editprofile(){
    print(_nameController.text);
    print(_emailController.text);
    print(_contactController.text);
    print(_addressController.text);
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
    body:Padding(
    padding:const EdgeInsets.all(20.0),
    child:Column(
      children:[
        Text('User editprofile'),
        TextFormField(
          controller: _nameController,
          decoration: InputDecoration(
          hintText:'Enter Name'
        ),
        ),
        TextFormField(
          controller: _emailController,
          decoration: InputDecoration(
          hintText:'Enter Email'
        ),
        ),
        TextFormField(
          controller: _contactController,
          decoration: InputDecoration(
          hintText:'Enter Contact'
        ),
        ),
        TextFormField(
          controller: _addressController,
          decoration: InputDecoration(
          hintText:'Enter Address'
        ),
        ),
        ElevatedButton(onPressed: (){
          editprofile();
        },child:Text('Save'))
      ],
    ),
    ),
    );
  }
}