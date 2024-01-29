import 'package:edupulse/firebase_options.dart';
import 'package:edupulse/splash_screen.dart';
import 'package:flutter/material.dart';
//file
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform
  );
  runApp(const MainApp());
}


class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home:splashscreen()
    );
  }
}