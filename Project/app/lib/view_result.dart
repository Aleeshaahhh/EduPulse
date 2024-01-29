import 'package:flutter/material.dart';
import 'package:edupulse/my_profile.dart';

class ViewResult extends StatefulWidget {
  const ViewResult({Key? key}) : super(key: key);

  @override
  State<ViewResult> createState() => _ViewResultState();
}

class _ViewResultState extends State<ViewResult> {
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
                MaterialPageRoute(
                  builder: (context) => const MyProfile(),
                ),
              );
            },
            icon: Icon(Icons.person),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: ListView(
          children: [
            Center(
              child: Container(
                padding: const EdgeInsets.all(20.0),
                width: 350,
                decoration: BoxDecoration(
                  color: Colors.lightBlueAccent,
                  borderRadius: BorderRadius.circular(20.0),
                ),
                child: Row(
                  children: [
                    Image.asset("assets/candidate1.jpg", width: 120, height: 150, fit: BoxFit.cover,),
                    const SizedBox(
                      height: 10,
                      width: 10,
                    ),
                    Column(
                      children: [
                        Text('Chairman'),
                        const SizedBox(
                          width: 10,
                        ),
                        Text('Candidate Name'),
                        const SizedBox(
                          width: 10,
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            Center(
              child: Container(
                padding: const EdgeInsets.all(20.0),
                width: 350,
                decoration: BoxDecoration(
                  color: Colors.lightBlueAccent,
                  borderRadius: BorderRadius.circular(20.0),
                ),
                child: Row(
                  children: [
                    Image.asset("assets/candidate2.jpg", width: 120, height: 150, fit: BoxFit.cover,),
                    const SizedBox(
                      height: 10,
                      width: 10,
                    ),
                    Column(
                      children: [
                        Text('Vice Chairman'),
                        const SizedBox(
                          width: 10,
                        ),
                        Text('Candidate Name'),
                        const SizedBox(
                          width: 10,
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            Center(
              child: Container(
                padding: const EdgeInsets.all(20.0),
                width: 350,
                decoration: BoxDecoration(
                  color: Colors.lightBlueAccent,
                  borderRadius: BorderRadius.circular(20.0),
                ),
                child: Row(
                  children: [
                    Image.asset("assets/candidate3.jpg", width: 120, height: 150, fit: BoxFit.cover,),
                    const SizedBox(
                      height: 10,
                      width: 10,
                    ),
                    Column(
                      children: [
                        Text('Secretary'),
                        const SizedBox(
                          width: 10,
                        ),
                        Text('Candidate Name'),
                        const SizedBox(
                          width: 10,
                        ),
                      ],
                    ),
                    const SizedBox(
                      height: 10,
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
