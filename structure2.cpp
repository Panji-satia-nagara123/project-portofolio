#include <iostream>

using namespace std;

struct siswa {
	string nama;
	string sekolah;
	unsigned int nis;
	
};

int main ()
{
	struct siswa siswa2;
	
	
	cout << "==++ Pendaftaran Siswa Baru ++==" << endl;
	cout << "Nama: ";
	getline(cin,siswa2.nama);
	
	cout << "sekolah: ";
	getline(cin,siswa2.sekolah);
	
	cout << "NIS: ";
	cin >> siswa2.nis;
	
	cout << endl;
	
	
	cout << "nama kamu "<< siswa2.nama << " dari " << siswa2.sekolah << " NIS " << siswa2.nis << endl;
	
	return 0;
	
}