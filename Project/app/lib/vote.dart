import 'package:flutter/material.dart';
import 'package:edupulse/my_profile.dart';

class Vote extends StatefulWidget {
  final TextEditingController _chairmanController = TextEditingController();
  final TextEditingController _uicchairmanController = TextEditingController();
  final TextEditingController _securityController = TextEditingController();

  void login() {
    print(_chairmanController.text);
    print(_uicchairmanController.text);
    print(_securityController.text);
  }

  @override
  State<Vote> createState() => _VoteState();
}

class _VoteState extends State<Vote> {
  String? selectedChairman;
  List<String> chairman = ['Hari', 'Das', 'Achu'];
  String? selectedViseChairman;
  List<String> viseChairman = ['Ameya', 'Niya', 'Ezra'];
  String? selectedSecretary;
  List<String> secretary = ['Daveed', 'Noah', 'John'];

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
                MaterialPageRoute(builder: (context) => const MyProfile()),
              );
            },
            icon: const Icon(Icons.person),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Container(
          padding: const EdgeInsets.all(20.0),
          height: 450,
          width: 500,
          decoration: BoxDecoration(
            color: Colors.lightBlueAccent,
            borderRadius: BorderRadius.circular(20.0),
          ),
          child: ListView(
            children: [
              const SizedBox(
                height: 20,
              ),
              const Center(
                child: Text(
                  'VOTE',
                  style: TextStyle(
                    fontSize: 20,
                    fontStyle: FontStyle.italic,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(
                height: 40,
              ),
              Row(
                children: [
                  const SizedBox(width: 100, child: Text('Chairman')),
                  Flexible(
                    child: DropdownButton<String>(
                      dropdownColor: Colors.white,
                      value: selectedChairman,
                      onChanged: (String? newValue) {
                        setState(() {
                          selectedChairman = newValue!;
                        });
                      },
                      isExpanded: true,
                      items: chairman.map((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(
                            value,
                            style: const TextStyle(color: Colors.black),
                          ),
                        );
                      }).toList(),
                    ),
                  ),
                ],
              ),
              const SizedBox(
                height: 20,
              ),
              Row(
                children: [
                  const Text('UIC Chairman'),
                  const SizedBox(
                width: 20,
              ),
                  Flexible(
                    child: DropdownButton<String>(
                      dropdownColor: Colors.white,
                      value: selectedViseChairman,
                      onChanged: (String? newValue) {
                        setState(() {
                          selectedViseChairman = newValue!;
                        });
                      },
                      isExpanded: true,
                      items: viseChairman.map((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(
                            value,
                            style: const TextStyle(color: Colors.black),
                          ),
                        );
                      }).toList(),
                    ),
                  ),
                ],
              ),
              const SizedBox(
                height: 20,
              ),
              Row(
                children: [
                  const Text('Secretary'),
                  const SizedBox(
                width: 20,
              ),
                  Flexible(
                    child: DropdownButton<String>(
                      dropdownColor: Colors.white,
                      value: selectedSecretary,
                      onChanged: (String? newValue) {
                        setState(() {
                          selectedSecretary = newValue!;
                        });
                      },
                      isExpanded: true,
                      items: secretary.map((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(
                            value,
                            style: const TextStyle(color: Colors.black),
                          ),
                        );
                      }).toList(),
                    ),
                  ),
                ],
              ),
              const SizedBox(
                height: 30,
              ),
              ElevatedButton(
                onPressed: () {
                  widget.login(); // Call the login method from the widget
                },
                child: const Text('VOTE'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
