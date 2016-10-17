#ifndef INC_PROFILER_H
#define INC_PROFILER_H

#include <string>
#include <map>
#include <windows.h>

#include<exception>

class Profiler
{
public:

	struct TimeData
	{
		TimeData():elapsedTime(0.0f)
		{}
		LARGE_INTEGER begin;
		LARGE_INTEGER end;
		float elapsedTime;
	};

	Profiler()
	{
		if(!QueryPerformanceFrequency(&m_TicksPerSecond))
		{
			throw std::runtime_error("Can't initialize timer.");
		}
	}

	void beginProfile(const std::string& name)
	{
		std::map<std::string,TimeData>::iterator it;
		if((it = m_Data.find(name)) != m_Data.end())
		{
			TimeData& time = it->second;
			QueryPerformanceCounter(&time.begin);
		}
		else
		{
			TimeData time;
			QueryPerformanceCounter(&time.begin);

			m_Data[name] = time;
		}

	}

	void endProfile(const std::string& name)
	{

		std::map<std::string,TimeData>::iterator it;

		if((it = m_Data.find(name)) != m_Data.end())
		{
			TimeData& time = it->second;


			QueryPerformanceCounter(&time.end);

			time.elapsedTime = ( (float) time.end.QuadPart - (float) time.begin.QuadPart) / (float) m_TicksPerSecond.QuadPart;
		}
	}

	float getData(const std::string& name)const
	{
		std::map<std::string,TimeData>::const_iterator it = m_Data.find(name);
		if(it!=m_Data.end())
			return it->second.elapsedTime;
		return 0.0f;
	}


	std::map<std::string,TimeData> m_Data;

	LARGE_INTEGER m_TicksPerSecond;
};



#endif // INC_PROFILER_H


