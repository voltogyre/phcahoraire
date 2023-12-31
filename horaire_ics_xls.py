# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# fait à partir de : https://regex101.com/r/08ft8p/1

import re

regex = r"BEGIN:VEVENT.*DESCRIPTION:(?<CAT>[^\n]+) Match #(?<MATCH_NO>[^\n]+)\n.*DTSTART;.*:(?<year>\d{4})(?<month>\d{2})(?<day>\d{2})T(?<hour>\d{2})(?<minute>\d{2})(?<sec>\d{2})\n.*DTEND;(?<DTEND>[^\n]+)\n.*LOCATION:(?<location>[^\n]+)\n.*SUMMARY;.*:(?<team_vis>[^\n]+) VS (?<team_loc>[^\n]+)\n.*END:VEVENT"

test_str = ("BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3557\n"
	"DTSTART;TZID=America/Toronto:20230928T144500\n"
	"DTEND;TZID=America/Toronto:20230928T154500\n"
	"LOCATION:Québec, Pavillon de la Jeunesse\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. Cardinal-Roy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3558\n"
	"DTSTART;TZID=America/Toronto:20231001T143000\n"
	"DTEND;TZID=America/Toronto:20231001T153000\n"
	"LOCATION:A.Samuel-Gagnon\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS Pavillon Wilbrod-Dufour\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3562\n"
	"DTSTART;TZID=America/Toronto:20231006T143000\n"
	"DTEND;TZID=America/Toronto:20231006T153000\n"
	"LOCATION:CS. DESJARDINS SSF (Aréna)\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS Séminaire Saint-François\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3569\n"
	"DTSTART;TZID=America/Toronto:20231017T130000\n"
	"DTEND;TZID=America/Toronto:20231017T140000\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Samuel-De Champlain VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3573\n"
	"DTSTART;TZID=America/Toronto:20231020T130000\n"
	"DTEND;TZID=America/Toronto:20231020T140000\n"
	"LOCATION:Aréna Duberger\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. la Camaradière\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3576\n"
	"DTSTART;TZID=America/Toronto:20231025T151500\n"
	"DTEND;TZID=America/Toronto:20231025T161500\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Saint-Jean-Eudes VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3584\n"
	"DTSTART;TZID=America/Toronto:20231109T144500\n"
	"DTEND;TZID=America/Toronto:20231109T154500\n"
	"LOCATION:Québec, Pavillon de la Jeunesse\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. Cardinal-Roy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3587\n"
	"DTSTART;TZID=America/Toronto:20231116T144500\n"
	"DTEND;TZID=America/Toronto:20231116T154500\n"
	"LOCATION:CS. DESJARDINS SSF (Aréna)\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS Séminaire Saint-François\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3588\n"
	"DTSTART;TZID=America/Toronto:20231117T131500\n"
	"DTEND;TZID=America/Toronto:20231117T141500\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:Séminaire Saint-François VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3591\n"
	"DTSTART;TZID=America/Toronto:20231121T130000\n"
	"DTEND;TZID=America/Toronto:20231121T140000\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. la Camaradière VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3593\n"
	"DTSTART;TZID=America/Toronto:20231125T183000\n"
	"DTEND;TZID=America/Toronto:20231125T193000\n"
	"LOCATION:Saint-Henri\n"
	"SUMMARY;LANGUAGE=en-us:Pavillon Wilbrod-Dufour VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3598\n"
	"DTSTART;TZID=America/Toronto:20231201T160000\n"
	"DTEND;TZID=America/Toronto:20231201T170000\n"
	"LOCATION:Charlesbourg, Réjean-Lemelin\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. Saint-Jean-Eudes\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3600\n"
	"DTSTART;TZID=America/Toronto:20231204T110000\n"
	"DTEND;TZID=America/Toronto:20231204T120000\n"
	"LOCATION:Québec, Beauport, Marc-Simoneau 1\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. Samuel-De Champlain\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3603\n"
	"DTSTART;TZID=America/Toronto:20231208T151500\n"
	"DTEND;TZID=America/Toronto:20231208T161500\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:Pavillon Wilbrod-Dufour VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3606\n"
	"DTSTART;TZID=America/Toronto:20231213T130000\n"
	"DTEND;TZID=America/Toronto:20231213T140000\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Cardinal-Roy VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3611\n"
	"DTSTART;TZID=America/Toronto:20231219T133000\n"
	"DTEND;TZID=America/Toronto:20231219T143000\n"
	"LOCATION:Lévis, Aréna BSR\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Saint-Jean-Eudes VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3615\n"
	"DTSTART;TZID=America/Toronto:20240117T133000\n"
	"DTEND;TZID=America/Toronto:20240117T143000\n"
	"LOCATION:Lévis, Aréna BSR\n"
	"SUMMARY;LANGUAGE=en-us:Séminaire Saint-François VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3616\n"
	"DTSTART;TZID=America/Toronto:20240119T151500\n"
	"DTEND;TZID=America/Toronto:20240119T161500\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Cardinal-Roy VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3620\n"
	"DTSTART;TZID=America/Toronto:20240129T160000\n"
	"DTEND;TZID=America/Toronto:20240129T170000\n"
	"LOCATION:Arena de Boischatel\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. Saint-Jean-Eudes\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3624\n"
	"DTSTART;TZID=America/Toronto:20240209T110000\n"
	"DTEND;TZID=America/Toronto:20240209T120000\n"
	"LOCATION:Québec, Beauport, Marc-Simoneau 1\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. Samuel-De Champlain\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3625\n"
	"DTSTART;TZID=America/Toronto:20240213T143000\n"
	"DTEND;TZID=America/Toronto:20240213T153000\n"
	"LOCATION:Aréna Duberger\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS É. sec. la Camaradière\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3633\n"
	"DTSTART;TZID=America/Toronto:20240222T130000\n"
	"DTEND;TZID=America/Toronto:20240222T140000\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Samuel-De Champlain VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3636\n"
	"DTSTART;TZID=America/Toronto:20240225T143000\n"
	"DTEND;TZID=America/Toronto:20240225T153000\n"
	"LOCATION:A.Samuel-Gagnon\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. Pointe-Lévy VS Pavillon Wilbrod-Dufour\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT\n"
	"BEGIN:VEVENT\n"
	"CLASS:PUBLIC\n"
	"DESCRIPTION:M18 D2 Match #3640\n"
	"DTSTART;TZID=America/Toronto:20240301T151500\n"
	"DTEND;TZID=America/Toronto:20240301T161500\n"
	"LOCATION:Aréna de Lévis\n"
	"SUMMARY;LANGUAGE=en-us:É. sec. la Camaradière VS É. sec. Pointe-Lévy\n"
	"TRANSP:TRANSPARENT\n"
	"END:VEVENT")

subst = "$MATCH_NO\\t\"2023-24\"\\t$CAT\\tPartie\\t$year-$month-$day\\t$hour:$minute\\t60\\tMatch no #$MATCH_NO - $team_vis vs $team_loc à $location\\t$location\\t?$team_vis\\t?$team_loc"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE | re.DOTALL)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
