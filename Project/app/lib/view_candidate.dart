import 'package:edupulse/my_profile.dart';
import 'package:flutter/material.dart';

class ViewCandidate extends StatefulWidget {
  final String id;
  const ViewCandidate({super.key, required this.id});

  @override
  State<ViewCandidate> createState() => _ViewCandidateState();
}

class _ViewCandidateState extends State<ViewCandidate> {
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
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            Container(
              padding: const EdgeInsets.all(20.0),
              width: 500,
              decoration: BoxDecoration(
                color: Colors.lightBlueAccent,
                borderRadius: BorderRadius.circular(20.0),
              ),
              child: Row(
                children: [
                  Image.asset("assets/candidate1.jpg",
                      width: 120, height: 150, fit: BoxFit.cover),
                  const SizedBox(
                    height: 20,
                    width: 20,
                  ),
                  Column(
                    children: [
                      Text(
                        'Candidate Name',
                      ),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('Candidate Type'),
                      const SizedBox(
                        width: 20,
                      ),
                    ],
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                ],
              ),
            ),
            const SizedBox(
              height: 20,
            ),
            Container(
              padding: const EdgeInsets.all(20.0),
              width: 500,
              decoration: BoxDecoration(
                color: Colors.lightBlueAccent,
                borderRadius: BorderRadius.circular(20.0),
              ),
              child: Row(
                children: [
                  Image.asset("assets/candidate2.jpg",
                      width: 120, height: 150, fit: BoxFit.cover),
                  const SizedBox(
                    height: 20,
                    width: 20,
                  ),
                  Column(
                    children: [
                      Text('Candidate Name'),
                      const SizedBox(
                        width: 20,
                      ),
                      Text('CandidateType'),
                      const SizedBox(
                        width: 20,
                      ),
                    ],
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
