import 'package:edupulse/dashboard.dart';
import 'package:edupulse/forgot_password.dart';
import 'package:edupulse/registration.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:fluttertoast/fluttertoast.dart';
// import 'package:edupulse/dashboard.dart';

class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}
class _LoginState extends State<Login> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  Future<void> login() async {
    print(_emailController.text);
    print(_passwordController.text);
    try {
        final FirebaseAuth auth = FirebaseAuth.instance;
        final UserCredential userCredential =
            await auth.signInWithEmailAndPassword(
          email: _emailController.text.trim(),
          password: _passwordController.text.trim(),
        );
        Navigator.push(context, MaterialPageRoute(builder: (context) => const Dashboard(),));
      } catch (e) {
        // Handle login failure and show an error toast.
        String errorMessage = 'Login failed';

        if (e is FirebaseAuthException) {
          errorMessage = e.code;
        }

        Fluttertoast.showToast(
          msg: errorMessage,
          toastLength: Toast.LENGTH_SHORT,
          gravity: ToastGravity.BOTTOM,
          backgroundColor: Colors.red,
          textColor: Colors.white,
        );
      }
    
  }
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
          child: Column(
            children:[
              const SizedBox(
                height: 50,
              ),
              const Text('Login',style: TextStyle(fontSize: 20,fontStyle: FontStyle.italic,fontWeight: FontWeight.bold),),
              const SizedBox(
                height: 40,
              ),
              TextFormField(
                controller: _emailController ,
                decoration: const InputDecoration(
                  hintText: 'Enter Email'
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              TextFormField(
                controller: _passwordController ,
                obscureText: true,
                decoration: const InputDecoration(
                  hintText: 'Enter Password'
                ),
              ),
              const SizedBox(
                height: 20,
              ),
              GestureDetector(
                onTap: (){
                 Navigator.push(context, MaterialPageRoute(builder: (context) => const ForgotPassword(),)); 
                },
                child: const Text('Forgot Password?')),
              const SizedBox(
                height: 20,
              ),
              ElevatedButton(onPressed: (){
                login();
              }, child: const Text('Login')),
              const SizedBox(
                height: 30,
              ),
              GestureDetector(
                onTap: (){
                 Navigator.push(context, MaterialPageRoute(builder: (context) => const Registration(),)); 
                },
                child: const Text('Create an account?'))
            ],
          ),
        ),
      ),
    );
    }
}
    // void gotodashboard() {
      // Navigator.push(context, MaterialPageRoute(builder: (context) => const Dashboard(),));
// }
      