# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.5541)
- **Original**: आः् 11 ] प्राव्यां दिज्लि शिरइशर्स्त याम्यायामथ वा नूप । सदैब स्वपतः पुंसो विपरीत तु रोगदम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5542)
- **Original**: 113 ऋतावुपगमइशस्तस्स्वपत्यामवनीपते । पुन्नामर्शे शुभे काले य्येष्ठायुग्मासु रात्रिषु
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5543)
- **Original**: 114 नाझूनां तु ख्त्रियं गच्छेन्नातुरां न रजस्वलाम्‌ । नानिष्टां न प्रकुपितां न त्रस्तां न च गर्भिणीम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5544)
- **Original**: 115 नादक्षिणां नान्यकामां नाकामां नान्ययोषितम्‌ क्षुत््षामों नातिभुक्तां वा स्वयं चैमिर्गुणैर्युतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5545)
- **Original**: 116 खातस्ख्रगान्यधृवक्प्रीतो नाध्मातः क्षुधितोअपि वा । सकामस्सानुरागश्ष व्यवायं पुरुषों व्रजेत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5546)
- **Original**: 117 चतुर्दश्यष्टमी चैव तथामा चाथ पूर्णिमा । पर्वाण्बेतानि राजेन्द्र रविसंक्रान्तिरित चे ।। 118 तैलख्रीमांससम्भोगी सर्वेश्वेतेषु खे पुमान्‌ । विण्मृत्नभोजन नाम प्रयाति नरक॑ मृतः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5547)
- **Original**: 119 अश्येषपर्वस्वेतेषु. तस्मात्संयपिभिर्तुणै: । भाव्यं सच्छास्रदेवेज्याध्यानजप्यपरैनरें:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5548)
- **Original**: 120 नान्ययोनाबयोनौ वा नोपयुक्तौषधस्तथा । द्विजदेवगुरूणां च व्यवायी नाश्रमे भवेत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5549)
- **Original**: 121 चैत्यचत्वरतीर्थेषु नैब गोष्ठे चतुष्पथे। नैय इमशानोपवने सलिलेषु महीपते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5550)
- **Original**: 122 प्रोक्तपर्वस्वशेषेषु नैव भूपाल सम्ध्ययो: । गक्ेद्ययवाय्य॑ मतिमान्न प्ूज्नोच्चारपीडित:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5551)
- **Original**: 123 पर्वस्वभिगमो5धन्यो दिबा पापप्रदो नृष । भुवि रोगावह्मे नृणामप्रशस्तो जलाशये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5552)
- **Original**: 124 परदारान्न गच्छेश मनसापि कथन । किमु वाचास्थिवन्धो5पि नास्ति तेषु व्यवायिनाप्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5553)
- **Original**: 125 तृतीय अंश 199 या जिसपर कुछ बिछा हुआ न हो उस द्वाय्यापर न स्रोबे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5554)
- **Original**: हे नृप ! सोनेके समय सदा पूर्व अथवा दक्षिणकी ओर सिर रखना चाहिये । इनके विपरीत दिज्नाओंकी ओर सिर रखनेसे रोगोंकी उत्पत्ति होती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5555)
- **Original**: हे पृथ्वीपते ! ऋतुकालमें अपनी ही स्त्रीसे सड्र करना उचित है। पुँल्लिक नक्षत्रमें युग्म और उनमें भी पीछेकी रात्रियॉमें शुभ समयमें स्त्रीप्रसक़ करे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5556)
- **Original**: किन्तु यदि स्त्री अप्रसन्ना, रोगिणी, रजसख्ला, निरभिलाषिणी, क्रोधिता, दुःस्थिनी अथवा गर्भिणी हो तो उसका सज्ञ न करे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5557)
- **Original**: जो सीधे स्वभावकी न हो, पराभिलाधिणी अथवा निरभिलाषिणी हो, क्षुघार्ता हो, अधिक भोजन किये हुए हो अथवा परखी हो उसके पास न जाय; और यदि अपनेमें ये दोष हों तो भी स्न्रीगमन न करे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5558)
- **Original**: पुरुषको उचित है कि स्त्रान करनेके अनन्तर माल्या और गन्ध घारण कर काम और अनुरगयुक्त होकर स्नीगमन करे । जिस समय अति भोजन किया हो अथवा क्षुधित हो उस समय उसमें ज्रवत्त न हो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5559)
- **Original**: हे राजेन्र ! चतुर्दशी, अष्टमी, अमावास्या, पूर्णिमा और सूर्यकी संक्रान्ति--ये सब पर्वदिन हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5560)
- **Original**: इन पर्वदिनोंमें तैछ, ख्री अथवा मोौसका भोग करनेवास्धा पुरुष मरनेपर विष्ठा और मूत्रसे भरे नरकमें पड़ता है
- **Translation**: 

---

