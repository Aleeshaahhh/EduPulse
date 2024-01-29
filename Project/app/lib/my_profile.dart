import 'package:edupulse/change_password.dart';
import 'package:edupulse/edit_profile.dart';
import 'package:flutter/material.dart';

class MyProfile extends StatefulWidget {
  const MyProfile({super.key});

  @override
  State<MyProfile> createState() => _MyProfileState();
}

class _MyProfileState extends State<MyProfile> {
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Container(
          padding: const EdgeInsets.all(20.0),
          height: 500,
          width: 500,
          decoration: BoxDecoration(
            color: Colors.transparent,
            borderRadius: BorderRadius.circular(20.0)
          ),
          child: ListView(
            children:[
              const SizedBox(
                height: 50,
              ),
              const Text('My Profile',style: TextStyle(fontSize: 20,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold),),
              const SizedBox(
                height: 40,
              ),
              Text('Name'),
              const SizedBox(
                height: 20,
              ),
              Text('Email'),
              const SizedBox(
                height: 20, 
              ),
              Text('Contact'),
              const SizedBox(
                height: 20, 
              ),
              Text('Address'),
              const SizedBox(
                height: 20, 
              ),
              
              GestureDetector(
                onTap: (){
                 Navigator.push(context, MaterialPageRoute(builder: (context) => const editprofile(),)); 
                },
                child: const Text('Edit Profile')),
              const SizedBox(
                height: 20,
              ),
              GestureDetector(
                onTap: (){
                 Navigator.push(context, MaterialPageRoute(builder: (context) => const ChangePassword(),)); 
                },
                child: const Text('Change Password'))
            ],
          ),
        ),
      ),
    );
    }
    void gotoeditprofile() {
      Navigator.push(context, MaterialPageRoute(builder: (context) => const editprofile(),));

  }
  void gotchangepassword() {
      Navigator.push(context, MaterialPageRoute(builder: (context) => const ChangePassword(),));

  }
}