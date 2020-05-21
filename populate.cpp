#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <random>
#include <fstream>
#include <ctime>
#include <string>
#include <cmath>

using namespace std;

random_device rd;
mt19937 generator(rd());

void printVector(vector<double> item)
{
	for(int i=0; i<item.size(); i++)
	{
		cout << item[i] << endl;
	}
}

int main(int argc, char *argv[])
{
	srand(time(NULL));   

	double radius = atof(argv[1]);
	double boxSize = atof(argv[2]);
	int N = atoi(argv[3]);

	vector<double> coordinates;

	uniform_real_distribution<> distribution(radius, boxSize-radius);
	float position = distribution(generator);

	for(int i=0; i<3; i++)
	{
		position = distribution(generator);
		coordinates.push_back(position);
	}

	vector<vector<double> > spheres;
	spheres.push_back(coordinates);

	while(spheres.size() < N)
	{
		vector<double> coordinatesNew;
		for(int i=0; i<3; i++)
		{
			position = distribution(generator);
			coordinatesNew.push_back(position);
		}

		int check = 0;
		for(int i=0; i<spheres.size(); i++)
		{
			if ( sqrt((spheres[i][0] - coordinatesNew[0]) +\
				  (spheres[i][1] - coordinatesNew[1]) +\
				  (spheres[i][2] - coordinatesNew[2])) > radius*2 )
			{
				check = check + 0;
			}
			else
			{
				check++;
			}
		}

		if(check == 0)
		{
			spheres.push_back(coordinatesNew);
		}

	}

	ofstream myfile;
	myfile.open("data.dat");
	for(int i=0; i<spheres.size(); i++){
		myfile << spheres[i][0] << "," << spheres[i][1] << "," << spheres[i][2] << "\n";
	}
	myfile.close();
	
	return 0;
}
