import 'package:edupulse/my_profile.dart';
import 'package:edupulse/view_candidate.dart';
import 'package:edupulse/view_result.dart';
import 'package:edupulse/vote.dart';
import 'package:flutter/material.dart';
class Dashboard extends StatefulWidget {
  const Dashboard({Key? key}) : super(key: key);

  @override
  State<Dashboard> createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('EDUPULSE'),
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const MyProfile()),
              );
            },
            icon: Icon(Icons.person), // Replace with the desired icon
          ),
        ],
      ),
       body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Container(
          padding: const EdgeInsets.all(20.0),
          height: 800,
          width: 800,
          decoration: BoxDecoration(
              color: Colors.transparent,
              borderRadius: BorderRadius.circular(20.0)),
          child: ListView(
            children: [
              Center(child: Image.asset("assets/voter.jpg")),
              const SizedBox(
                height: 20,
              ),
              Center(child: Text('HELLO,username',style: TextStyle(fontSize: 25.0),)),
              const SizedBox(
                height: 50,
              ),
              GestureDetector(
                onTap: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context) => Vote(),)); 
              },
              child:Container(
                decoration:BoxDecoration (borderRadius: BorderRadius.circular(15),color:Colors.lightBlueAccent,),
                height: 100,
                width: 100,
                child: Center(child: Text('VOTE',style: TextStyle(fontSize: 30,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold),)),
              ),
              ),
              const SizedBox(
                height: 20,
              ),
              GestureDetector(
                onTap: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context) => const viewcandidate(),)); 
              },
              child:Container(
                decoration:BoxDecoration (borderRadius: BorderRadius.circular(15),color:Colors.lightBlueAccent,),
                height: 100,
                width: 100,
                child: Center(child: Text('VIEW CANDIDATE',style: TextStyle(fontSize: 30,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold),)),
              ),
              ),
              const SizedBox(
                height: 20,
              ),
              GestureDetector(
                onTap: (){
                  Navigator.push(context, MaterialPageRoute(builder: (context) => const ViewResult(),)); 
              },
              child:Container(
                decoration:BoxDecoration (borderRadius: BorderRadius.circular(15),color:Colors.lightBlueAccent,),
                height: 100,
                width: 100,
                child: Center(child: Text('VIEW RESULT',style: TextStyle(fontSize: 30,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold),)),
              ),
              ),
            ],
          ),
        ),
      ),
    );
  }
} 