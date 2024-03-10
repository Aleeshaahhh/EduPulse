import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:edupulse/my_profile.dart';
import 'package:edupulse/view_candidate.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:progress_dialog_null_safe/progress_dialog_null_safe.dart';
import 'package:fluttertoast/fluttertoast.dart';

class Election extends StatefulWidget {
  const Election({super.key});

  @override
  State<Election> createState() => _ElectionState();
}

class _ElectionState extends State<Election> {
  List<Map<String, dynamic>> electionList = [];
  late ProgressDialog _progressDialog;
  @override
  void initState() {
    super.initState();
    _progressDialog = ProgressDialog(context);
    // getData();
  }

  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  Future<void> candidateApply(id) async {
    _progressDialog.show();

    print(id);
    final user = FirebaseAuth.instance.currentUser;
    final userId = user?.uid;
    DateTime now = DateTime.now();
    String formattedDate = DateFormat('yyyy-MM-dd').format(now);
    Map<String, dynamic> data = {
      'student_id': userId,
      'election_id': id,
      'candidate_status': 0,
      'submission_date': formattedDate,
      'winner': false,
      // Add other fields as needed
    };
    // Collection reference
    CollectionReference classCandidateCollection =
        _firestore.collection('tbl_class_candidate');

    // Add data to the collection
    classCandidateCollection.add(data).then((value) {
      _progressDialog.hide();
      Fluttertoast.showToast(
        msg: "Candidate Applied",
        toastLength: Toast.LENGTH_SHORT,
        gravity: ToastGravity.BOTTOM,
        backgroundColor: Colors.green,
        textColor: Colors.white,
      );
      print("Data added successfully!");
    }).catchError((error) {
      _progressDialog.hide();
      Fluttertoast.showToast(
        msg: "Something went wrong",
        toastLength: Toast.LENGTH_SHORT,
        gravity: ToastGravity.BOTTOM,
        backgroundColor: Colors.red,
        textColor: Colors.white,
      );
      print("Error adding data: $error");
    });
  }

  Future<void> getData() async {
    try {
      electionList = [];
      // Reference to the collection
      CollectionReference<Map<String, dynamic>> electionCollection =
          FirebaseFirestore.instance.collection('tbl_election');

      // Get documents from the collection
      QuerySnapshot<Map<String, dynamic>> querySnapshot =
          await electionCollection.get();

      // Iterate through the documents and add them to the list
      querySnapshot.docs
          .forEach((QueryDocumentSnapshot<Map<String, dynamic>> doc) {
        Map<String, dynamic> data = doc.data();
        // Add the document ID as 'election_id' to the data
        data['election_id'] = doc.id;
        electionList.add(data);
      });

      // Print the list for testing (you can remove this in the final version)
      print(electionList);
    } catch (e) {
      print('Error fetching data: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('EDUPULSE'),
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
            icon: const Icon(Icons.person),
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: FutureBuilder(
          future: getData(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              // Loading indicator or placeholder can be added here
              return const CircularProgressIndicator();
            } else if (snapshot.hasError) {
              // Display an error message
              return Text('Error: ${snapshot.error}');
            } else {
              return ListView.builder(
                itemCount: electionList.length,
                itemBuilder: (context, index) {
                  Map<String, dynamic> electionData = electionList[index];
                  // Your existing itemBuilder code
                  return Container(
                    padding: const EdgeInsets.all(20.0),
                    width: 500,
                    decoration: BoxDecoration(
                      color: Colors.lightBlueAccent,
                      borderRadius: BorderRadius.circular(20.0),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('Date: ${electionData['election_for_date']}'),
                        const SizedBox(
                          height: 5,
                        ),
                        Text('${electionData['election_details']}'),
                        const SizedBox(
                          height: 5,
                        ),
                        Text(
                            'Last Date: ${electionData['election_nomination_ldate']}'),
                        const SizedBox(
                          height: 20,
                        ),
                        Row(
                          children: [
                            Flexible(
                              child: ElevatedButton(
                                  onPressed: () {
                                    Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                          builder: (context) => ViewCandidate(
                                              id: electionData[
                                                  'election_for_date']),
                                        ));
                                  },
                                  child: const Text('View Candidates')),
                            ),
                            Flexible(
                              child: ElevatedButton(
                                  onPressed: () {},
                                  child: const Text('View Results')),
                            ),
                            Flexible(
                              child: ElevatedButton(
                                  onPressed: () {
                                    candidateApply(electionData['election_id']);
                                  },
                                  child: const Text('Apply')),
                            ),
                          ],
                        )
                      ],
                    ),
                  );
                },
              );
            }
          },
        ),
      ),
    );
  }
}
