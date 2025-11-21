#include <iostream>

using namespace std;

struct siswa {
	string nama;
	string jeniskelamin;
	unsigned int uangsaku;
	
};

int main ()
{
	struct siswa siswa1;
	siswa1.nama = "panji satia";
	siswa1.jeniskelamin = "cowok ";
	siswa1.uangsaku = 100000 ;
	
	cout << siswa1.nama << " jenis kelaminya " << siswa1.jeniskelamin << endl;
	cout << "diberi uang saku " << siswa1.uangsaku << " per hari " << endl;
	
	return 0;
	
}