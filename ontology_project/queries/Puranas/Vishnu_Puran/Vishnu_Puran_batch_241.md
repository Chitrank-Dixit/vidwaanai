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

### Verse 1 (Vishnu Puran 0.4801)
- **Original**: 198 जातुकणों5भवन्पत्त: कृष्णद्वैपायनस्तत: अष्टाबिशितिरित्येते बेदव्यासा: पुरातना:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4802)
- **Original**: 19 एको बेद्तुर्भा तु तेः कृतो द्वापरादिषु
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4803)
- **Original**: 20 भर्िष्ये द्वापरे चापि द्रौणिव्यासो भविष्यति । व्यतीते मम्त पुत्रेडस्मिन्‌ कृष्णबैपायने मुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4804)
- **Original**: 219 घुवमेकाक्षरं ब्रह्म ओमित्येव व्यवस्थितम्‌ । यृहत्वादबृंहणत्वाथध तदल्रह्मेत्यभिधीयते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4805)
- **Original**: 22 प्रणवावस्थितं नित्य भूर्भुवस्स्वरितीर्यते । ऋग्यजुस्सामाधर्वाणो यत्तस्मै ब्रह्मणे नमः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4806)
- **Original**: 23 हैं--वह मुझसे सुनो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4807)
- **Original**: इस उैवस्वत-मन्वन्तरफे प्रत्येक द्वापरयुगमें व्यास महर्पियोंने अबतक पुनः-पुनः अद्ठाईस बार वेटॉंके विभाग किये हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4808)
- **Original**: हे साधुग्रेष्ठ ! जिन्होंने पुनः-पुनाः द्वापरयुगमें बेदोँके चार चार विभाग किये हैं उन अद्ठाईस व्यासॉका विवरण सुनो ---
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4809)
- **Original**: पहले द्वापरमें स्वय॑ भगवान्‌ ब्रह्माजीने वेटरॉका विभाग किया था। दूसरे द्वापरके वेदव्यास प्रजापति हुए
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4810)
- **Original**: तीसरे ड्वापरमें शुक्राचार्यजी और चौथेमें बृहस्पतिजी व्यास हुए, तथा पाँचवेंमें सूर्य और छठेसें भगवान्‌ मृत्यु व्यास कहत्खये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4811)
- **Original**: सातवें द्वापस्के वेदव्यास इन्द्र, आठवेंके वसिष्ठ, न्वेंके सारस्वत और दसरवेंके त्रिधामा कहे जाते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4812)
- **Original**: ग्यारहवेंमें त्रिदिख, बारतवेंमें भरद्वाज, तेरहवेंमें अन्तरिक्ष और चौदहवेंमें वर्णों नामक व्यास हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4813)
- **Original**: प्डावेंमें प्रय्यारण, सोलहवेंमें घनज॒य, सत्रह॒वेंमें क्रुक़्य और तदनत्तर अठारहतेंमें जय नामक्क व्यास हुए
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4814)
- **Original**: फिर उन्नीसलें व्यास भरद्वाज हुए, भरद्वाजके पीछे गौतम हुए और गौठपक्ते पीछे जो व्यास हुए के हर्यात्पा कहे जाते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4815)
- **Original**: हर्यात्पाफे अनन्तर वाजश्रवामुनि ख्यास हुए तथा उनके पश्चात्‌ सोमशुष्मवशी तृणबिन्द्‌ (तेईसर्वें) वेदव्यास कड़लाये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4816)
- **Original**: उनके पीछे भृगुबंशी ऋक्ष व्यास हुए जो वाल्मीकि कहल्आये, तदनन्तर हमारे पिता शक्ति हुए और फिर मैं हुआ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4817)
- **Original**: मेरे अनन्तर जातुकर्ण व्यास हुए और फिर कृष्णद्वैपायन--इस प्रकार ये अड्डाईस व्यास प्राचीन हैं। इन्होंने द्वापरादि युणोंगें एक हो वेदके चार-चार विभाग किये हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4818)
- **Original**: हे मुने! मेरे पुत्र कृष्णट्रैपायनके अनन्तर आगामी ड्वापरयुगमें द्रोण-पुत् अश्वत्थामा वेदव्यास होंगे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4819)
- **Original**: 3# यह अविनाशी एकाक्षर ही ब्रह्मा है । यह बुहत्‌ और ज्यापक है इसल्य्ये 'ब्रह्म' कहत्मता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4820)
- **Original**: भुलेंक, भुवर्लेक और स्वर्लेक्र- ये तीनों फ्रणवरूप ब्रह्ममें ही स्थित हैं तथा प्रणन हो ऋक्‌, यजुः, साम और अशर्वरूप है; अतः उस ऑकाररूप ब्रह्मकों नमस्कार है
- **Translation**: 

---

