// ConsoleApplication.cpp : main project file.

//#include <Windows.h>
#include "stdafx.h"
#include "ConsoleHelper.h"
#include <fstream>
#include <string>
#include <cstring>
#include <iostream>
#include <sstream>
#include <vector>
#include <time.h>

//using namespace std;
using namespace System;
using namespace System::IO;
using namespace Threading;

//Global X and Y print positions
int posX = 0, posY = 0;

#pragma region Funcoes
void SetPosition(int x, int y) {
	posX = x; posY = y;
	Console::SetCursorPosition(x, y);
}

void Print(std::string toPrint) {
	//cout << toPrint;
	String^ str2 = gcnew String(toPrint.c_str());
	ConsoleHelper::ImprimirASCIIExtended(posX, posY, ConsoleColor::Black, ConsoleColor::Yellow, str2);
	SetPosition(posX + toPrint.length(), posY);
}

String^ spiner(int value) {
	Console::BackgroundColor = ConsoleColor::Black;
	Console::ForegroundColor = ConsoleColor::Yellow;

	if(value == 0) return "/";
	else if(value == 1) return "-";
	else if(value == 2) return "\\";
	else if(value == 3) return "|";

	Console::ForegroundColor = ConsoleColor::Green;
	return "OK";
}


void PrintSpiner(int posX, int posY, int spinerint, String^ str) {
	if(spinerint != 5)
		ConsoleHelper::ImprimirASCIIExtended(posX, posY, ConsoleColor::Black, ConsoleColor::Yellow, "[ " + spiner(spinerint) + " ] - " + str);
	else {
		ConsoleHelper::ImprimirASCIIExtended(posX, posY, ConsoleColor::Black, ConsoleColor::Yellow, "[ ");
		ConsoleHelper::ImprimirASCIIExtended(posX + 2, posY, ConsoleColor::Black, ConsoleColor::Green, "OK");
		ConsoleHelper::ImprimirASCIIExtended(posX + 4, posY, ConsoleColor::Black, ConsoleColor::Yellow, " ] - " + str);
	}
}

Char GetKey() {
	return Console::ReadKey().KeyChar;
}

ConsoleKeyInfo GetKeyInfo() {
	return Console::ReadKey(true);
}

void GetLineIntoString(String^ *str, int posX, int posY) {
	while(true) {
		ConsoleHelper::ImprimirASCIIExtended(0, 0, ConsoleColor::Black, ConsoleColor::Yellow, *str);
		ConsoleKeyInfo input = Console::ReadKey();
		if(input.Key == ConsoleKey::Enter) break;
		else {
			*str += input.KeyChar;
		}
	}
}

void ReturnInputIntoString(String^ *str) {
	ConsoleKeyInfo keyInfo;
	keyInfo = Console::ReadKey(true);
	*str += keyInfo.KeyChar;
}

void PrintGreen(std::string str) {
	String^ str2 = gcnew String(str.c_str());
	ConsoleHelper::ImprimirASCIIExtended(posX, posY, ConsoleColor::Green, ConsoleColor::Black, str2);
	SetPosition(posX + str.length() + 1, posY);
}

std::string ToString(int value) {
	std::string out_string;
	std::stringstream ss;
	ss << value;
	out_string = ss.str();
	return out_string;
}

void CLEAR() {
	Console::BackgroundColor = ConsoleColor::Black;
	Console::ForegroundColor = ConsoleColor::White;
	Console::Clear();
}

enum Screens {
	menu, check, setup, closeApp
};

void CheckFile(String^ file, int *intSpiner) {
	if(!File::Exists(file)) {
		*(intSpiner) += 1;
		if(*(intSpiner) >= 4) *(intSpiner) = 0;
	}
	else {
		*(intSpiner) = 5;
	}
}

#pragma endregion

int main(cli::array<System::String ^> ^args) {

	int w = 100, h = 20;
	char spin_chars[] = "/-\\|";
	Screens screen = menu;

	Console::SetWindowSize(w, h);
	Console::SetBufferSize(w, h);

	std::string fileName = "index.html";

#pragma region VARIABLES
	//BASIC INFO
	std::string PageTitle = "";
	std::string Name = "";
	std::string Website = "";
	std::string Description = "";

	std::string Developer = "";
	std::string DeveloperLink = "";
	std::string BasedIn = "";
	std::string FoundingDate = "";
	std::string PressContactEmail = "";
	std::string Phone = "";
	std::vector<std::string> SocialsName;
	std::vector<std::string> SocialsLink;
	std::string Address = "";

	std::string aux;

	//HISTORY PART
	std::string EarlyHistory = "";
	std::string AfterThat = "";
	std::vector<std::string> ProjectName;
	std::vector<std::string> ProjectLink;

	//VIDEOS
	std::vector<std::string> VideoLink;
	std::vector<std::string> VideoComent;

	//IMAGES
	std::string ImagesComent = ""; //Text
	int ImagesCount = 10; //Coment + Link "number of images"
	int LogoCount = 10;

	//AWARDS
	std::vector<std::string> Awards;

	//ARTICLES
	std::vector<std::string> SelectedArticles;
	std::vector<std::string> ArticleAutor;

	//TEAM
	std::vector<std::string> TeamMember;
	std::vector<std::string> MemberFunc;
#pragma endregion

	if(!Directory::Exists("./images"))
		Directory::CreateDirectory("./images");


	while(true) {
		if(screen == menu) {

			// MENU
			Console::Clear();

			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 3, ConsoleColor::Black, ConsoleColor::Yellow, "+------------------------------------------ +");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 4, ConsoleColor::Black, ConsoleColor::Yellow, "|               WELLCOME TO                 |");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 5, ConsoleColor::Black, ConsoleColor::Yellow, "|                                           |");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 6, ConsoleColor::Black, ConsoleColor::Yellow, "|         HTML PRESSKIT GENERATOR           |");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 7, ConsoleColor::Black, ConsoleColor::Yellow, "+------------------------------------------ +");

			ConsoleHelper::ImprimirASCIIExtended(7, 14, ConsoleColor::Black, ConsoleColor::Yellow, "[1] - CHECK IF YOU HAVE MAKE EVEERYTHING	 [2] - SETUP HTML TEXTS	[ESC] - EXIT");

			ConsoleKeyInfo input = Console::ReadKey(true);

			if(input.Key == ConsoleKey::D1)
				screen = check;
			else if(input.Key == ConsoleKey::D2)
				screen = setup;
			else if(input.Key == ConsoleKey::Escape) {
				screen = closeApp;
			}

		}

		else if(screen == check) {
			//CHECK IF HAS EVERYTHING
			int favcon = 0, header = 0, oneimage = 0, imagesZip = 0, oneLogo = 0, logoZip = 0;
			int posX = 20;

			while(true) {


				Console::Clear();
				ConsoleHelper::ImprimirASCIIExtended((w / 2) - 25, 3, ConsoleColor::Black, ConsoleColor::Yellow, "+ CHECKING IF YOU HAVE EVERYTHING ON THE FOLDER +");

				//cli::array<System::String ^>^ b = System::IO::Directory::GetFiles("./images");

				CheckFile("./images/favicon.png", &favcon);
				CheckFile("./images/header.png", &header);
				CheckFile("./images/img_0.png", &oneimage);
				CheckFile("./images/images.zip", &imagesZip);
				CheckFile("./images/logo_0", &oneLogo);
				CheckFile("./images/logos.zip", &logoZip);


				//Required actions
				PrintSpiner(posX, 6, favcon, "UPLOAD TO /images a FAVICON (favicon.png)");
				PrintSpiner(posX, 7, header, "UPLOAD TO /images A HEADER IMAGE (1200x240px - header.png)");
				PrintSpiner(posX, 8, oneimage, "UPLOAD TO /images AT LEAST ONE IMAGE");
				PrintSpiner(posX, 9, oneLogo, "UPLOAD TO /images A logo.png");

				PrintSpiner(posX, 11, imagesZip, "MAKE A images.zip FILE IN /images WITH THE IMAGES TO DOWNLOAD");
				PrintSpiner(posX, 12, logoZip, "MAKE A logo.zip WITH IN /images WITH LOGOS VARIATIONS TO DOWNLOAD");

				ConsoleHelper::ImprimirASCIIExtended((w / 2) - 10, 16, ConsoleColor::Black, ConsoleColor::Yellow, "[ESC] - GO TO MENU");


				if(Console::KeyAvailable) {
					if(Console::ReadKey().Key == ConsoleKey::Escape) {
						screen = menu;
						break;
					}
				}

				Thread::Sleep(100); //10segundos (16)
			}
		}

		else if(screen == setup) {

			CLEAR();

		#pragma region BASIC INFO
			SetPosition(w / 4, 1);
			std::cout << " =============== BASIC INFO ===============";

			SetPosition(2, 3);
			Print("HTML PAGE TITLE: ");
			//std::cin.ignore();
			std::getline(std::cin, PageTitle);
			PrintGreen(PageTitle);

			SetPosition(2, 5);
			Print("COMPANY/GAME NAME: ");
			std::getline(std::cin, Name);
			PrintGreen(Name);

			//SetPosition(2, 7);
			Print("WEBSITE: https://www.");
			std::getline(std::cin, Website);
			posX -= 12;
			PrintGreen("https://www." + Website);

			SetPosition(2, 7);
			Print("DESCRIPTION: ");
			std::getline(std::cin, Description);
			PrintGreen(Description);

			SetPosition(2, 9);
			Print("DEVELOPER: ");
			std::getline(std::cin, Developer);
			PrintGreen(Developer);

			Print("DEVELOPER LINK: https://www.");
			std::getline(std::cin, DeveloperLink);
			posX -= 12;
			PrintGreen("https://www." + DeveloperLink);

			SetPosition(2, 11);
			Print("BASED IN: ");
			std::getline(std::cin, BasedIn);
			PrintGreen(BasedIn);

			Print("ADDRESS: ");
			std::getline(std::cin, Address);
			PrintGreen(Address);

			SetPosition(2, 13);
			Print("FOUNDING DATE: ");
			std::getline(std::cin, FoundingDate);
			PrintGreen(FoundingDate);

			SetPosition(2, 15);
			Print("CONTACT E-MAIL: ");
			std::getline(std::cin, PressContactEmail);
			PrintGreen(PressContactEmail);

			Print("CONTACT PHONE: ");
			std::getline(std::cin, Phone);
			PrintGreen(Phone);

			CLEAR();
			SetPosition(w / 4, 1);
			std::cout << " =============== BASIC INFO ===============";

			SetPosition(2, 3);
			int numberOfSocials = 0;
			Print("Number of Social Networks: ");
			std::cin >> numberOfSocials;
			std::cin.ignore();
			for(int i = 0; i < numberOfSocials; i++) {
				SetPosition(4, 5 + i + 1);

				Print("Name [" + ToString(i + 1) + "]: ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				SocialsName.push_back(aux);

				Print("Link : https://www.");
				std::getline(std::cin, aux);
				posX -= 12;
				PrintGreen("https://www." + aux);
				SocialsLink.push_back(aux);
			}


		#pragma endregion
		#pragma region HISTORY PART
			CLEAR();

			SetPosition(w / 4, 1);
			std::cout << " =============== HISTORY PART ===============";

			SetPosition(2, 3);
			Print("Early History: ");
			std::getline(std::cin, EarlyHistory);
			PrintGreen(EarlyHistory);

			SetPosition(2, 5);
			Print("AfterThat: ");
			std::getline(std::cin, AfterThat);
			PrintGreen(AfterThat);

			int numberOfProjects = 0;
			SetPosition(2, 7);
			Print("Number of Projects to Put with link: ");
			std::cin >> numberOfProjects;
			std::cin.ignore();

			for(int i = 0; i < numberOfProjects; i++) {
				SetPosition(4, 7 + i + 1);

				Print("Project [" + ToString(i + 1) + "]: ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				ProjectName.push_back(aux);

				Print("Link (https or dinamic path): ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				ProjectLink.push_back(aux);
			}

		#pragma endregion

		#pragma region VISUAL RESOURCES - VIDEOS, IMAGES, LOGOS

			CLEAR();

			SetPosition(w / 4, 1);
			std::cout << " =============== VISUAL RESOURCES ===============";

			int numberOfVideos = 0;
			SetPosition(2, 3);
			Print("Number of VIDEOS do you whant to put: ");
			std::cin >> numberOfVideos;
			std::cin.ignore();

			if(numberOfVideos >= 9) numberOfVideos = 9;

			for(int i = 0; i < numberOfVideos; i++) {
				SetPosition(2, 5 + i);
				//foiAte += i + 1;
				Print("Video [" + ToString(i + 1) + "] Coment: ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				VideoComent.push_back(aux);

				Print("Link: https://www.");
				std::getline(std::cin, aux);
				PrintGreen("https://www." + aux);
				VideoLink.push_back(aux);

			}

			if(posY + 7 > 20) {
				CLEAR();
				SetPosition(w / 4, 1);
				std::cout << " =============== VISUAL RESOURCES ===============";
				posY = 3;
			}

			SetPosition(2, posY + 2);
			Print("Number of IMAGES do you whant to put: ");
			std::cin >> ImagesCount;
			std::cin.ignore();
			std::cout << std::endl;

			SetPosition(2, posY + 1);
			Print("[REMEMBER TO RENAME THE IMAGES TO img_0, img_1,  img_2,  ...]");

			SetPosition(2, posY + 2);
			Print("Number of LOGOS do you whant to put: ");
			std::cin >> LogoCount;
			std::cin.ignore();

			SetPosition(2, posY + 1);
			Print("[REMEMBER TO RENAME THE LOGOS TO logo_0, logo_1, logo_2, ...]");
			Console::ReadKey(true);

		#pragma endregion

		#pragma region Awards & Recognition

			CLEAR();

			SetPosition(w / 4, 1);
			std::cout << " =============== AWARDS & RECOGNITION ===============";

			int numberOfAwards = 0;
			SetPosition(2, 3);
			Print("Number of AWARDS do you whant to put: ");
			std::cin >> numberOfAwards;
			std::cin.ignore();

			SetPosition(2, 4);
			for(int i = 0; i < numberOfAwards; i++) {
				SetPosition(2, posY + 1);

				Print("Award [" + ToString(i + 1) + "] Coment: ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				Awards.push_back(aux);

				posY += 1;

				if(posY + 3 > h && i + 1 < numberOfAwards) {
					CLEAR();
					SetPosition(w / 4, 1);
					std::cout << " =============== AWARDS & RECOGNITION ===============";
					SetPosition(2, 3);
					Print("Number of TEAM MEMBERS do you whant to put: " + ToString(numberOfAwards));
					SetPosition(2, 4);
				}
			}

		#pragma endregion

		#pragma region SELECTED ARTICLES

			CLEAR();
			SetPosition(w / 4, 1);
			std::cout << " =============== SELECTED ARTICLES ===============";

			int numberOfArticles = 0;
			SetPosition(2, 3);
			Print("Number of ARTICLES do you whant to put: ");
			std::cin >> numberOfArticles;
			std::cin.ignore();

			SetPosition(2, 4);
			for(int i = 0; i < numberOfArticles; i++) {
				SetPosition(2, posY + 1);
				Print("Article [" + ToString(i + 1) + "]: ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				SelectedArticles.push_back(aux);

				SetPosition(4, posY + 1);
				Print("Autor [" + ToString(i + 1) + "]: - ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				ArticleAutor.push_back(aux);

				posY += 1;

				if(posY + 3 > h && i + 1 < numberOfArticles) {
					CLEAR();
					SetPosition(w / 4, 1);
					std::cout << " =============== SELECTED ARTICLES ===============";
					SetPosition(2, 3);
					Print("Number of ARTICLES do you whant to put: " + ToString(numberOfArticles));
					SetPosition(2, 4);
				}

			}

		#pragma endregion

		#pragma region TEAM

			CLEAR();
			SetPosition(w / 4, 1);
			std::cout << " =============== TEAM MEMBERS ===============";

			int numberOfMembers = 0;
			SetPosition(2, 3);
			Print("Number of TEAM MEMBERS do you whant to put: ");
			std::cin >> numberOfMembers;
			std::cin.ignore();

			SetPosition(2, 4);
			for(int i = 0; i < numberOfMembers; i++) {
				SetPosition(2, posY + 1);
				Print("Member Name [" + ToString(i + 1) + "]: ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				TeamMember.push_back(aux);

				SetPosition(2, posY + 1);
				Print("Mamber Func [" + ToString(i + 1) + "]: - ");
				std::getline(std::cin, aux);
				PrintGreen(aux);
				MemberFunc.push_back(aux);

				posY += 1;

				if(posY + 3 > h && i + 1 < numberOfMembers) {
					CLEAR();
					SetPosition(w / 4, 1);
					std::cout << " =============== TEAM MEMBERS ===============";
					SetPosition(2, 3);
					Print("Number of TEAM MEMBERS do you whant to put: " + ToString(numberOfMembers));
					SetPosition(2, 4);
				}

			}

		#pragma endregion

		#pragma region CONTACT - NEED????

			//NEED ??


		#pragma endregion

		#pragma region GENERATE HTML


			std::ofstream myfile;
			myfile.open("./" + fileName);

			myfile << "<!DOCTYPE html>" << std::endl << " <html>" << std::endl << "	<head>" << std::endl << std::endl;
			myfile << "	<!-- Required meta tags -->" << std::endl;
			myfile << "	<meta charset = 'utf-8'>" << std::endl;
			myfile << "	<meta name='viewport' content='width = device-width, initial-scale = 1, shrink-to-fit = no'>" << std::endl;
			myfile << "	<!-- Bootstrap CSS -->" << std::endl << std::endl << "	<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css' integrity='sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO' crossorigin='anonymous'>" << std::endl << std::endl;


			myfile << "	<title> " << PageTitle << " </title>" << std::endl;
			myfile << "	<link rel='shortcut icon' href='images/favicon.png'>" << std::endl << std::endl;
			myfile << "</head>" << std::endl << "<body>" << std::endl << std::endl;

			//LEFT BAR
			myfile << "<div class='container'>" << std::endl;
			myfile << "	<div class='row'>" << std::endl;
			myfile << "		<div class='col col-lg-3  p-3 mb-2 bg-white text-dark' style='font-family:Trebuchet MS; '>" << std::endl;
			myfile << "			<p class='h2' style='font-family:Trebuchet MS; '>" << Name << "</p>" << std::endl;
			myfile << "			<a href='https://www." << Website << "' target='_blank'>" << Website << "</a>" << std::endl;
			myfile << "			<br><br>" << std::endl << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#factsheet'>Factsheet</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#description'>Description</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#history'>History</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#projects'>Projects</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#videos'>Videos</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#images'>Images</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#logo'>Logo & Icon</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#awards'>Awards & Recognition</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#articles'>Selected Articles</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#credits'>Team</a>" << std::endl;
			myfile << "			<a class='btn btn-light btn-sm btn-block text-left' href='#contact'>Contact</a>" << std::endl;
			myfile << "		</div>" << std::endl;
			myfile << "		<div class='col-sm' style='font-family:Trebuchet MS;'>" << std::endl;
			myfile << "			<img src='images/header.png' class='img-fluid' alt='Responsive image'>" << std::endl;
			myfile << "			<div class='row'>" << std::endl;
			myfile << "				<div class='col col-lg-4'>" << std::endl;
			myfile << "					<br><p class='h4' style='font-family:Georgia; 'id='factsheet'>Factsheet</p>" << std::endl;
			myfile << "					<br><p class='font-weight-normal' >" << std::endl;
			myfile << "					Developer: <br>" << std::endl;
			myfile << "					<a href='https://www." << DeveloperLink << "'>" << Developer << "</a> <br>" << std::endl;
			myfile << "					" << BasedIn << "</p>" << std::endl;
			myfile << "					<p class='font-weight-normal'>" << std::endl;
			myfile << "					Founding date: <br>" << std::endl;
			myfile << "					" << FoundingDate << "</p>" << std::endl;
			myfile << "					<p class='font-weight-normal'>" << std::endl;
			myfile << "					Website: <br>" << std::endl;
			myfile << "					<a href=https://www.'" << Website << "' target='_blank'>" << Website << "</a><p>" << std::endl;
			myfile << "					<p class='font-weight-normal'>" << std::endl;
			myfile << "					Press / Business contact: <br>" << std::endl;
			myfile << "					<a href='mailto:" << PressContactEmail << "'>" << PressContactEmail << "</a><p>" << std::endl;
			myfile << "					<p class='font-weight-normal'>" << std::endl;
			myfile << "					Social: <br>" << std::endl;

			for(int i = 0; i < SocialsName.size(); i++)
				myfile << "					<a href='https://www." << SocialsLink.at(i) << "' target='_blank'> " << SocialsName.at(i) << " </a> <br>" << std::endl;

			myfile << "					</p>" << std::endl;
			myfile << "					<p class='font-weight-normal'>" << std::endl;
			myfile << "					Releases: <br> <!-- Criar presskit para os games bons-->" << std::endl;

			//MUDAR PARA RELEASES
			for(int i = 0; i < ProjectName.size(); i++)
				myfile << "					<a href='" << ProjectLink.at(i) << "' target='_blank'>" << ProjectName.at(i) << "</a> <br>" << std::endl;

			myfile << "					</p>" << std::endl;
			myfile << "				</div>" << std::endl;

			//DESCRICAO
			myfile << "				<div class='col-sm'>" << std::endl;
			myfile << "					<br><p class='h4' style='font-family:Georgia;' id='description'> Description</p>" << std::endl;
			myfile << "					<p>" << Description << "</p>" << std::endl;
			myfile << "					<br><p class='h4' style='font-family:Georgia;' id='history'> History</p>" << std::endl;
			myfile << "					<p class='font-weight-bold font-italic'>Early history</p>" << std::endl;
			myfile << "					<p>" << std::endl;
			myfile << "					" << EarlyHistory << std::endl;
			myfile << "					<br>" << std::endl;
			myfile << "					<p class='font-weight-bold font-italic'>After that</p>" << std::endl;
			myfile << "					" << AfterThat << std::endl;
			myfile << "					</p>" << std::endl;
			myfile << "					<br><p class='h4' style='font-family:Georgia;' id='projects'>Projects</p>" << std::endl;
			for(int i = 0; i < ProjectName.size(); i++)
				myfile << "					&emsp; &middot; <a href='https://www." << ProjectLink.at(i) << "' target='_blank'>" << ProjectName.at(i) << "</a> <br>" << std::endl;

			myfile << "				</div>" << std::endl;
			myfile << "			</div>" << std::endl;

			//VIDEOS
			myfile << "			<hr>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='videos'> Videos</p>" << std::endl;
			for(int i = 0; i < VideoLink.size(); i++) {
				myfile << "			<p class='font-italic'>" << VideoComent.at(i) << "" << std::endl;
				myfile << "			<a href='https://www." << VideoLink.at(i) << "' target='_blank'> Youtube </a> </p>" << std::endl;
				myfile << "			<iframe width=100% height='315' src='https://www." << VideoLink.at(i) << "' frameborder='0' allow='autoplay; encrypted-media' allowfullscreen></iframe>" << std::endl;
			}

			//PHOTOS
			myfile << "			<hr>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='images'>Images</p>" << std::endl;
			myfile << "			<div class='alert alert alert-primary' role='alert'>" << std::endl;
			myfile << "			<a href='images/images.zip'>download all screenshots & photos as .zip(2 MB)</a>" << std::endl;
			myfile << "			</div>" << std::endl;
			myfile << "			<picture>" << std::endl;
			for(int i = 0; i < ImagesCount; i++) {
				if(i % 2 == 0) myfile << "				<img src='images/img_" << i << ".png' class='rounded img-fluimages/id' width=48.7%>" << std::endl;
				else {
					myfile << "				<img src='images/img_" << i << ".png' class='rounded img-fluimages/id float-right' width=48.7%>" << std::endl;
					myfile << "				<br><br>" << std::endl;
				}

			}

			myfile << "			</picture>" << std::endl;
			myfile << "			<br><br><p>" << std::endl;
			myfile << "			" << ImagesComent << std::endl;
			myfile << "			<a href='mailto:" << PressContactEmail << "' target='_blank'>Make Contact!</a>" << std::endl;
			myfile << "			</p>" << std::endl;

			//LOGOS
			myfile << "			<hr>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='logo'>Logo & Icon</p>" << std::endl;
			myfile << "			<div class='alert alert alert-primary' role='alert'>" << std::endl;
			myfile << "			<a href='images/logo.zip'>download logo files as .zip(1 MB)</a>" << std::endl;
			myfile << "			</div>" << std::endl;
			myfile << "			<picture>" << std::endl;
			for(int i = 0; i < LogoCount; i++) {
				if(i % 2 == 0) myfile << "				<img src='images/logo_" << i << ".png' class='rounded img-fluimages/id' width=48.7%>" << std::endl;
				else {
					myfile << "				<img src='images/logo_" << i << ".png' class='rounded img-fluimages/id float-right' width=48.7%>" << std::endl;
					myfile << "				<br><br>" << std::endl;
				}

			}
			myfile << "			</picture>" << std::endl;
			myfile << "			</p>" << std::endl;

			//AWARDS
			myfile << "			<hr>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='awards'>Awards & Recognition</p>" << std::endl;
			for(int i = 0; i < Awards.size(); i++)
				myfile << "			<p> &middot; " << Awards.at(i) << "</p>" << std::endl;

			//SELECTED ARTICLES
			myfile << "			<hr>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='articles'>Selected Articles</p>" << std::endl;
			for(int i = 0; i < SelectedArticles.size(); i++)
				myfile << "			<p> &middot; '" << SelectedArticles.at(i) << "'<br>" << std::endl << "&emsp; -" << ArticleAutor.at(i) << "</p>" << std::endl;

			//TEAM
			myfile << "			<hr>" << std::endl;
			myfile << "			<div class='row'>" << std::endl;
			myfile << "			<div class='col col-lg-6'>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='credits'>Team & Repeating Collaborator</p>" << std::endl;
			for(int i = 0; i < TeamMember.size(); i++)
				myfile << "			<p>" << TeamMember.at(i) << "<br>" << MemberFunc.at(i) << "</p>" << std::endl;

			//CONTACT
			myfile << "		</div>" << std::endl;
			myfile << "		<div class='col-sm'>" << std::endl;
			myfile << "			<br><p class='h4' style='font-family:Georgia;' id='contact'>Contact</p>" << std::endl;
			myfile << "			<p>Inquiries<br>" << std::endl;
			myfile << "			<a href='mailto:" << PressContactEmail << "'>" << PressContactEmail << "</a></p>" << std::endl;

			for(int i = 0; i < SocialsName.size(); i++) {
				myfile << "			<p>" << SocialsName.at(i) << "<br>" << std::endl;
				myfile << "			<a href='https://www." << SocialsLink.at(i) << "' target='_blank'> " << SocialsLink.at(i) << " </a></p>" << std::endl;
			}

			myfile << "			<p>Web<br>" << std::endl;
			myfile << "			<a href='https://www." << Website << "' target='_blank'>" << Website << "</a></p>" << std::endl;
			myfile << "		</div>" << std::endl;
			myfile << "	</div>" << std::endl;

			myfile << "	<hr> <p> Done with *HTMLPressKitGenerator* by Andre Jeller <a href='https://www.andrejeller.com' target='_blank1'>(AJS)</a> - using <a href='http://dopresskit.com/' target='_blank'>DoPresskit()</a> by model</p>" << std::endl;
			myfile << "			" << std::endl;

			//Closing
			myfile << "	</div>" << std::endl;
			myfile << "</div></div>" << std::endl;



			myfile << "</body></html>" << std::endl;
		#pragma endregion

			CLEAR();

			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 3, ConsoleColor::Black, ConsoleColor::Yellow, "+------------------------------------------ +");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 4, ConsoleColor::Black, ConsoleColor::Yellow, "|            YOU HAVE FINISHED              |");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 5, ConsoleColor::Black, ConsoleColor::Yellow, "|             THE SETUP PART                |");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 6, ConsoleColor::Black, ConsoleColor::Yellow, "|  CHECK IN MENU IF YOU FOGUET SOMETHING    |");
			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 23, 7, ConsoleColor::Black, ConsoleColor::Yellow, "+------------------------------------------ +");

			ConsoleHelper::ImprimirASCIIExtended((w / 2) - 13, 10, ConsoleColor::Black, ConsoleColor::Yellow, "[ANY BUTTON] - GO TO MENU");

			Console::ReadKey(true);
			screen = menu;
		}

		else if(screen == closeApp) {
			return 0;
		}
	}

	return 0;
}