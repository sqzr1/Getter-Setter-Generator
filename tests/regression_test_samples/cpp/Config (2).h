/// \file config.h
/// \author Jared Chidgey

#ifndef DYNAMIC_CONFIG_H
#define DYNAMIC_CONFIG_H

#include <map>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

/// \brief Class that contains configurational data, refernced by a string name.

/// This class represents a set of configuration data. The data is mapped to a name
/// The most important part of the class is it's abiltity to parse this data from a file.
/// Current functionality: Managerment, writes back to file, commment parsing,
/// multiple and custom comment styles, supports different data types.

typedef class Dynamic_Config
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//coment styles
		/// \brief Array hold all the different type of comment styles.
		std::vector<std::string>								comment_styles;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//data
		/// \brief Holds a token, and associated int data.
		std::map<std::string, int> 								data_int;

		/// \brief Holds a token and associated floating point data.
		std::map<std::string, float> 							data_float;

		/// \brief Holds a token, and associated string data.
		std::map<std::string, std::string> 						data_string;

		/// \brief Holds comments.
		std::map<std::string, std::string>						comments;

		/// \brief Relays whether data was found.
		bool													found;

		/// \brief Current active data header fro io
		std::string												data_header;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Dynamic_Config();

		/// \brief Non-standard class constructor, loading from file(string).
																Dynamic_Config(std::string filename);

		/// \brief Class destructor.
																~Dynamic_Config();
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//comnfig file options
		/// \brief Adds a custom comment style.
		bool													add_comment_style(std::string new_c);

		/// \brief Support functino
		/// if a function retuns a not found token, this function
		/// conveys whether that was actually valid, or was a coincidence.
		inline bool												data_found()
																{
																	return found;
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//get data
		/// \brief Returns integer data
		bool													get_int(std::string name, int &target);

		/// \brief Returns float data.
		bool													get_float(std::string name, float &target);

		/// \brief Returns string data.
		bool													get_string(std::string name, std::string &target);

		/// \brief Returns comment.
		bool													get_comment(std::string name, std::string &target);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//add data
		/// \brief Adds data item. Returns false if token exists
		bool													add_int(std::string name, int val);

		/// \brief Adds float data, returns false if token exists.
		bool													add_float(std::string name, float val);

		/// \brief Adds string data, returns false if token exitsts.
		bool													add_string(std::string name, std::string val);

		/// \brief Adds a comment, only for existing data tokens.
		bool													add_comment(std::string name, std::string words);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//remove data
		/// \brief Removes data from the config file.
		bool													remove_data(std::string name);

		/// \brief Removes a comment from the file.
		bool													remove_comment(std::string name);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//modify
		/// \brief  Modifies an existing int.
		bool													modify_int(std::string name, int new_val);

		/// \brief Modifies an existing float.
		bool													modify_float(std::string name, float new_val);

		/// \brief Modifies an existing string.
		bool													modify_string(std::string name, std::string new_val);

		/// \brief Modifies an existing comment
		bool													modify_comment(std::string name, std::string new_val);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//printing
		/// \brief Prints all data to a string, and returns it.
		std::string												print_to_string();

		/// \brief prints to string incuding comments.
		std::string												print_to_string_com();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Writes a config file to a text file.
		bool													write(std::string filename);

		bool													debug_write(std::string filename);

		/// \brief	Parses data froma commented config file.
		bool													read(std::string filename);

		bool													debug_read(std::string filename);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//constants
		//Internal type reading headers
		static const std::string								HEADER_INT;
		static const std::string								HEADER_FLOAT;
		static const std::string								HEADER_STRING;

		//Null returns, if these are returned,.
		//check the data_found() function.
		static const int										NO_INT = -1;
		static const float										NO_FLOAT;
		static const std::string								NO_STRING;

		//standard comeent styles
		static const std::string								COMMENT_1;
		static const std::string								COMMENT_2;
		static const std::string								COMMENT_3;
		static const int										COMMENT_STYLES = 3;
		//-------------------------------------------------------------------------------//

}CONFIG,*PCONFIG;

#endif // DYNAMIC_CONFIG_H
