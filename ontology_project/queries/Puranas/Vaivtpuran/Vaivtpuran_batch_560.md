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

### Verse 1 (Vaivtpuran 39.8219)
- **Original**: क्षण कैलासपर जा पहुँचे। वहाँ उन्होंने अत्यन्त
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8220)
- **Original**: उसकी रचना की थी। उसमें होरे जड़े हुए थे। रमणीय परम मनोहर नगर देखा। वह नगर ऐसी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8221)
- **Original**: वह पंद्रह योजन ऊँचा और चार योजन विस्तृत बड़ी-बड़ी सड़कोंसे सुशोभित था, जो अत्यन्त
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8222)
- **Original**: था। उसके चारों ओर अत्यन्त सुन्दर सुडौल भली लगती थीं। उनकी भूमि सोनेकी भूमिकी-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8223)
- **Original**: चौकोर परकोटा बना हुआ था। दर्वाजोंपर नाना सी थी, जिनपर शुद्ध स्फटिकके सदृश मणियाँ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8224)
- **Original**: प्रकारकी चित्रकारियोंसे युक्त रत्नोंके किवाड़ लगे जड़ी हुई थीं। उस नगरमें चारों ओर सिंदूरकी-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8225)
- **Original**: थे। वह उत्तम मणियोंकी वेदियोंसे युक्त तथा सी रंगवाली मणियोंकी वेदिकाएँ बनी थीं। वह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8226)
- **Original**: मणियोंके खंभोंसे सुशोभित था। राशि-की-राशि मुक्ताओंसे संयुक्त और मणियोंके, . नारद! परशुरामने उस आश्रमके प्रधानद्वारके मण्डपोंसे परिपूर्ण था। उसमें यक्षोंके एक अरब
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8227)
- **Original**: दाहिनी ओर वृषेन्द्रको और बायीं ओर सिंह तथा दिव्य भवन थे, जो रत्नों और काझनोंसे परिपूर्ण,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8228)
- **Original**: नन्दीश्वर, महाकाल, भयंकर पिंगलाक्ष, विशालाक्ष, यक्षेन्द्रणणोंसे परिवेष्टित और मणिनिर्मित किवाड़,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8229)
- **Original**: बाण, महाबली विरूपाक्ष, विकटाक्ष, भास्कराक्ष, खम्भे और सीढ़ियोंसे शोभायमान थे। वह नगर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8230)
- **Original**: रक्ताक्ष, विकटोदर, संहारभैरव, भयंकर कालभैरव, दिव्य सुवर्ण-कलशों, चाँदीके बने हुए श्वेत
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8231)
- **Original**: रुक्भैरद, ईशकौ-सी आभावाले महाभैरव, चँवरों, रत्रोंके आभूषणोंसे विभूषित था। वह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8232)
- **Original**: कृष्णाड्रभैरव, दृढपराक्रमी क्रोधभैरव, कपालभैरव, उद्दी्त होती हुई सुन्दरियों, हाथोंमें चित्रलिखित
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8233)
- **Original**: रुद्रभैरव तथा सिद्धेद्नों, रुद्रगणों, विद्याधरों, गुह्मकों, पुत्तलिकाएँ लिये हुए निरन्तर स्वच्छन्दतापूर्वक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8234)
- **Original**: भूतों, प्रेतों, पिशाचों, कृष्माण्डों, ब्रह्मरक्षसों, वेतालों, हँसते और खेलते हुए सुन्दर-सुन्दर बालकों एवं
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8235)
- **Original**: दानवों, जटाधारी योगीद्धों, यक्षों, किंपुरुषों और बालिकाओं तथा स्वर्गगड़ाके तटपर उगे हुए
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8236)
- **Original**: किन्नरोंको देखा। उन्हें देखकर भृगुनन्दनने उनके पारिजातके वृक्षसमूहोंसे खचाखच भरा था।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8237)
- **Original**: साथ वार्तालाप किया। फिर नन्दिकेश्वरकी आज्ञा सुगन्थित एवं खिले हुए पुष्पसमूहोंसे सम्पन्न,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8238)
- **Original**: ले वे प्रसन्न मनसे भीतर घुसे। आगे बढ़नेपर उन्हें कल्यवृक्षोंका आश्रय लेनेवाले कामधेनुसे पुरस्कृत,
- **Translation**: 

---

