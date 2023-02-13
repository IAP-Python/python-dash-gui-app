---

# Documentation

### This here is an informal compilation of notes, reminders, dates, and other things related to this investigation. Normally you would keep track of these things by some kind of progress report every week but, that's too formal, this is my way of progress report without the formalities.

For starters these are the people involved:

* 


## Meeting 2 (October 13)

I was at a funeral while recording the meeting that was streamed from my tablet and recording it from my phone, so apologies for the background noise, my aunt died.

Transcription sanitized and translated to english:

TI Engineer: We collect the data, at different conditions, limits, etc. We want to characterize the device in question. We use a user interface, a GUI that contains many instruments, like the power supply to variate voltage, oscilloscopes to measure signals \[...]. Different test require different tests require different conditions, like for example changing temperature. We have a heat gun and heat the device at, say, 125 degrees Celsius, we turn the device on, and we measure the signal. These signals are recorded under a file of .tdms format.

* Note
    .tdms files are files typically generated from Labview.

     For about 2 to 3 minutes the engineer fiddles around to show us an example of what this file would look like. The file he sent us is about 200MB, give or take. A pretty larger file for what is simply a custom csv file. He's not used to using Google meet.

    The TI engineer was during his vacations while holding this meeting, and we the students were in recess because of a strike and some power outage issues... again.

TI Engineer: This report right here, report 0B045 (remember to attach file ), in my opinion from the ones I worked on, the most detailed because it contains many graphs, its fully complete. Obviously just skim throgh it you don't need to sit down and read the whole thing, rather, familiarize with what the report is saying and the core concepts it brings that you would need for this project. So, the 044 is the last report at the date that I finished. So, I sent you the data that comes with this last report and I sent it so you have it as a point of reference.



## Jan 31, 2023

I separated the app into two main components:
- frontend
- backend

Basically the idea is that anything related to the manipulation of data is independent from the programming of the UI/UX. Reason is because it was making me go mad :,)

Anyway, I got the group names sanitized and the load pretty fast. I also got the filtering of said groups working using regex. I'm still missing the UI implementation Pepe designed on a diagram app as concept

Because I don't know what conventions TI will use in the future I made a YAML config file. It should work in conjuction with the regex filter

I used (this)[https://jsonformatter.org/yaml-validator] YAML file validator to make sure it works. Hopefully the way it works is simple-stupid enough for non-tech ppl.