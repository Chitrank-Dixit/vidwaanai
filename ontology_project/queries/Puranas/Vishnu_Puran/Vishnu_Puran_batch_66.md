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

### Verse 1 (Vishnu Puran 0.1301)
- **Original**: 21 अ्रीपरदार उवाच ता प्र्ापवतीमेव वाष्पाकुलविलोचनाम्‌। समाहितमना विष्णौ पश्यन्नपि न दृष्टवान्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1302)
- **Original**: 22 वत्स वत्स सुघोराणि रक्षांस्थेतानि भीषणे । वने&भ्युद्यतशखस्त्राणि समायान्त्यपगम्यथताम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1303)
- **Original**: 23 ततो नादानतीयोग्रान्नाजपुत्रस्य ते पुरः। मुमुचुर्दीप्शत्नाणि भ्रामयन्तो निशाचरा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1304)
- **Original**: 25 शिवाश्व शतझो नेदु: सज्वालाकबलैमुखे: । ऋ्रासाय तस्य बालंस्थ योगयुक्तस्य सर्वदा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1305)
- **Original**: 26 हन्यतां हन्यतामेष छिद्यतां छिद्यतामयम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1306)
- **Original**: भक्ष्यतां भक्ष्यतां चायमित्यूजुस्ते निश्ञालरा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1307)
- **Original**: 27 ततो नानाविथान्नादान्‌ सिंहोष्टमकरानना: । आ्रासाय राजपुत्रस्य नेदुस्ते रजनीचरा:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1308)
- **Original**: 28 रक्षांसि तानि ते नादाः झिवास्तान्यायुधानि न । गोविन्दासक्तचित्तस्थ ययुर्नेन्द्रियगोचरम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1309)
- **Original**: 29 एकाग्रचेता: सतत विष्णुमेबात्मसंश्रयम्‌। दृष्टबान्यूधिवीनाथपुत्रो नान्‍्य॑ कथझ्जन
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1310)
- **Original**: 30 श्रोविष्णुपुतण ( अ* 12 [ उसने कहा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1311)
- **Original**: --बेटा ! तू शरीरकों घुल्मनेवाले इस भयद्भर तपका आयह छोड दे। मैने बड़ी-बड़ों कामनाओंद्वारा तझे प्राम किया है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1312)
- **Original**: ओरे ! सुझ अकेली, अनाथा, दुस्वियाको सौतके कद वाक्योंसे छोड़ देना तुझे उचित नहीं है। बेटा ! मुझ आश्रयहीनाका तो एकमात्र तू ही सहारा है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1313)
- **Original**: कहाँ तो पाँच वर्षका तू और कहाँ तेरा यह अति उग्र तप ? ओरे ! इस निष्फल क्लेज्ञ़कारी आग्रहसे अपना मन मोड़ छे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1314)
- **Original**: अभी तो तेरे खेलने-कुदनेका समय है, फिर अध्ययनका समय आयेगा, तदनन्तर समस्त भोगोंके भोगनेका और फिर अन्तमें तपस्या करना भी ठीक होगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1315)
- **Original**: बेटा ! तुझ सुकुमार बालकका 'जो स्वेल-कुृदका समय है उसीपें तू तपस्था करना चाहता है। तू इस प्रकार क्यों अपने सर्वनाशमें तत्पर हुआ है ?
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1316)
- **Original**: तेरा परम धर्म तो मुझको प्रसन्न रखना ही है, अतः तू अपनी आयु और अवस्थाके अनुकूल कर्मोंमें ही छग, मोहका अनुवर्तन न कर और इस तपरूपी अधर्मसे निशत्त हो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1317)
- **Original**: बेटा । यदि आज तू इस तपस्याको न छोड़ेगा तो देख्व तेरे सामने ही मैं अपने प्राण ऊेड़ दूँगी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1318)
- **Original**: भ्रीपराशरजी बोले--हे मैत्रेय ! भगवान्‌ विष्णुमें चित्त स्थिर रहनेके कारण घुवने उसे आँखोंमें आँसू भरकर इस प्रकार विलाप करतों देखकर भो नहीं देखा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1319)
- **Original**: तब, 'अरे बेटा ! यहाँसे भाग-भाग ! देख, इस महाभयड्डूर बनमें ये कैसे भोर राक्षस अख्न शस्त्र उठाये आ रहे हैं'--ऐसा कहतो हुई वह चली गयी और वहाँ जिनके मुखसे अभिकी लूपटें स्किल रही थीं ऐसे अनेकों राक्षसगण अखस््न-शस्त्र सैंभाले पकट हो गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1320)
- **Original**: डन राक्षसोने अपने अति चमकीछे दास्न्ोंको घुमाते हुए उस राजपुत्रके सापने बड़ा भयद्भर कोल्मृहछ किया
- **Translation**: 

---

