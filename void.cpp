#include <iostream>

using namespace std;

void sayHello() {
cout << "Halooo, ini void" << endl;
}
void sapa (string nama) {
cout << "Halooooo, " << nama << "!" << endl;
}

int main(){
	sayHello();
	sapa("panji");
	
	
	return 0;
}