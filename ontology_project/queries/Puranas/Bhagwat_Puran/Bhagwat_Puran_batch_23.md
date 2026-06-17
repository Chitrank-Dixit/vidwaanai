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

### Verse 1 (Bhagwat Puran 0.441)
- **Original**: तदनन्तर पितृगणका तर्पण कर पूर्व पापॉकी शुद्धिके लिये प्रायश्चित करे और एक मण्डल बनाकर उसमें श्रीहरिको स्थापित करें
- **Translation**: 

---

### Verse 2 (Bhagwat Puran 0.442)
- **Original**: फिर भगवान्‌ श्रीकृष्णको लक्ष्य करके मन्त्रोच्चारणपूर्वक क्रमशः षोडशोपचारविधिसे पूजन करे और उसके पश्चात्‌ प्रदक्षिणा तथा नमस्कारादि कर इस प्रकार स्तुति करे
- **Translation**: 

---

### Verse 3 (Bhagwat Puran 0.443)
- **Original**: “करुणानिधान ! मैं संसार-सागरमें डूबा हुआ और बड़ा दीन हूँ। कर्मोके मोहरूपी ग्राहने मुझे पकड़ रकखा है। आप इस संसार-सागरसे मेरा उद्धार कीजिये
- **Translation**: 

---

### Verse 4 (Bhagwat Puran 0.444)
- **Original**: इसके पश्चात्‌ धूप-दीप आदि सामग्रियोंसे श्रीमद्धागवतकी भी बड़े उत्साह और प्रीतिपूर्वक्क विधि-विधानसे पूजा करें
- **Translation**: 

---

### Verse 5 (Bhagwat Puran 0.445)
- **Original**: फिर पुस्तकके आगे नारियल रखकर नमस्कार करें और प्रसन्नच्त्तिसि इस प्रकार स्तुति करें--
- **Translation**: 

---

### Verse 6 (Bhagwat Puran 0.446)
- **Original**: 'श्रीमद्भागवतके रूपमें आप साक्षात्‌ श्रीकृष्णचन्द्र ही विराजमान हैं। नाथ ! मैंने भवसागरसे छुटकारा पानेके लिये आपकी शरण ली है
- **Translation**: 

---

### Verse 7 (Bhagwat Puran 0.447)
- **Original**: मेरा यह मनोरथ आप ब्रिना किसी विध्र-बाधाके साड्रोपाड़ पूरा करें । केशव ! मैं आपका दास हूँ'
- **Translation**: 

---

### Verse 8 (Bhagwat Puran 0.448)
- **Original**: इस प्रकार दीन वचन कहकर फिर वक्ताका पूजन करें। उसे सुन्दर वसख्राभूषणोंसे विभूषित करें और फिर पूजाके पश्चात्‌ उसकी इस प्रकार स्तुति करे--
- **Translation**: 

---

### Verse 9 (Bhagwat Puran 0.449)
- **Original**: 'शुकस्वरूप भगवन्‌ ! आप समझानेकी कलामें कुशल और सब शाखोँपें पारंगत हैं; कृपया इस कथाकों प्रकाशित करके मेरा अज्ञान टूर करें!
- **Translation**: 

---

### Verse 10 (Bhagwat Puran 0.450)
- **Original**: फिर अपने कल्याणके लिये प्रसन्नतापूर्वक उसके सामने नियम ग्रहण करे और सात दिनॉतक- यथाशक्ति उसका पालन करे
- **Translation**: 

---

### Verse 11 (Bhagwat Puran 0.451)
- **Original**: कथामें विशप्न न हो, इसके लिये पाँच ब्राह्णॉकों और वरण करे; वे द्वादशाक्षर मचद्वारा भगवान्के नामोंका जप करें
- **Translation**: 

---

### Verse 12 (Bhagwat Puran 0.452)
- **Original**: फिर ब्राह्मण, अन्य विष्णुभक्त एवं कीर्तन करनेबालॉको नमस्कार करके उनकी पूजा करें और उनकी आज्ञा पाकर ख्ये भी
- **Translation**: 

---

### Verse 13 (Bhagwat Puran 0.453)
- **Original**: 20 « श्रीमद्धागवत * (अ>् 6 अधोमेओओ ऑल मय ये ओ जय जे जे जय जय तय जय यकय तय घटित घी आय ले मे जय घ लेते ऑयल जे जय के औ औ के औ औ # हे हे औ औे के औ औ औ हे के और ओे औ ओ के कै औ की के के मे औ # # के आसनपर बैठ जाय
- **Translation**: 

---

### Verse 14 (Bhagwat Puran 0.454)
- **Original**: जो पुरुष लोक, सम्पत्ति, धन, घर और पुत्रादिकी चिन्ता छोड़कर शुद्धचित्तसे केवल कथामें ही ध्यान रखता है, उसे इसके श्रवणका उत्तम फल मिलता है
- **Translation**: 

---

### Verse 15 (Bhagwat Puran 0.455)
- **Original**: बुद्धिमान्‌ वक्ताको चाहिये कि सूर्योदयसे कथा आरम्प करके साढ़े तीन पहस्तक मध्यम स्वर्से अच्छी तरह कथा बाँचे
- **Translation**: 

---

### Verse 16 (Bhagwat Puran 0.456)
- **Original**: दोपहरके समय दो घड़ीतक कथा बंद रखे। उस समय कथाके प्रसड्के अनुसार वैष्णवोंकी भगवानके गुणोंका कीर्तन करना चाहिये--व्यर्थ बातें वहीं करनी चाहिये
- **Translation**: 

---

### Verse 17 (Bhagwat Puran 0.457)
- **Original**: कथाके समय मल-मूत्रके वेगको काबूमें रखनेके लिये अल्पाहार सुखकारी होता है; इसलिये श्रोता केवल एक ही समय हृविष्यान्न भोजन करे
- **Translation**: 

---

### Verse 18 (Bhagwat Puran 0.458)
- **Original**: यदि शक्ति हो तो सातों दिन निराहार रहकर कथा सुने अथवा केवल घो या दूध पीकर सुखपूर्वक श्रवण करे
- **Translation**: 

---

### Verse 19 (Bhagwat Puran 0.459)
- **Original**: अथवा फलाहार या एक समय ही भोजन करे। जिससे जैसा नियम सुभीतेसे सघ सके, उसीको कथाश्रवणकरे लिये ग्रहण करें
- **Translation**: 

---

### Verse 20 (Bhagwat Puran 0.460)
- **Original**: मैं तो उपवासकी अपेक्षा भोजन करना अच्छा समझता हूँ, यदि वह कथाश्रवणमें सहायक हो। यदि उपवाससे श्रवणमें बाधा पहुँचती हो तो वह किसी कामका नहीं
- **Translation**: 

---

