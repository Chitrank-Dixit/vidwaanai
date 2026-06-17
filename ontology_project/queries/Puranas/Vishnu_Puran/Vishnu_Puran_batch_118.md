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

### Verse 1 (Vishnu Puran 0.2341)
- **Original**: 98 इत्युवत्वा सो3भवन्‍्मौनी तेषां गौरवयन्त्रितः । प्रहस्य चर पुनः प्राह किमनन्तेन साध्विति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2342)
- **Original**: 19 साधु भो किमनन्तेन साधु भो गुरवो मम । श्रूयतां यदनन्तेन यदि खेद न यास्यथ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2343)
- **Original**: 20 धर्मार्थकाममोक्षाक्ष पुरुषार्था उदाहुताः । अतुष्टयमिद यस्मात्तस्मात्कि किमिदं व:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2344)
- **Original**: 29 प्ररीचिमिश्रैर्दक्षाह्रैस्तथैवान्यै रनन्तत: । धर्म: प्राप्तस्तथा चान्यैरथर्थ: कामस्तथाउपरै:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2345)
- **Original**: 22 तत्तत्त्तवेदिनो भूत्वा ज्ञानध्यानसमाधिप्रि: । अबापुर्मुक्तिपपरे पुरुषा ध्वस्तबन्धना:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2346)
- **Original**: 23 सम्पदैश्चर्यमाहात्म्यज्ञानसन्ततिकर्मणाम्‌_
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2347)
- **Original**: ब्िमुक्तेश्ेकतो लभ्य॑ मूलमाराथन हरे:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2348)
- **Original**: 24 यतो धर्मार्थकामाख्य॑ मुक्तिआपि फल द्विजा: । तेनापि कि किमित्येवमनन्तेन किमुच्यते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2349)
- **Original**: 25 कि चापि जहुनोक्तेन भवन्तो गुरवो मम । बल्तु साधु बासाधु विवेकोउस्माकमल्पकः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2350)
- **Original**: 26 श्रीविष्णुपुराण [ आ* 18 ही होगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2351)
- **Original**: इसलिये तुम यह विपक्षकी स्तुति करना छोड़ दो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2352)
- **Original**: तुम्हारे पिता सब प्रकार प्रशंसनीय हैं और वे ही समस्त गुरुओँमें परम गुरु हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2353)
- **Original**: च्रह्मदजी बोले--डे महाभागगण ! यह ठीक ही है। इस सम्पूर्ण जिस्नेकीमें भगवान्‌ मरीचिका यह महान्‌ कुल अवश्य ही प्रशंसनीय है। इसमें कोई कुछ भी अन्यथा नहीं कह सकता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2354)
- **Original**: और मेरे पिताजों भी सम्पूर्ण जगत्‌में बहुत बड़े पराक्रमी हैं; यह भी मैं जानता है यह यात भी बिछकुछ ठोक है, अन्यथा नहीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2355)
- **Original**: आपने जो कहा कि समस्त गुरुओंमें पिता ही परम गुरु हैं--इसमें भी मुझे लेशमात्र सन्देह नहीं है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2356)
- **Original**: पिताजी परम गुरु हैं और प्रयत्रपूर्वक पूजनीय हैं-- इसमें कोई सन्देह नहीं। और मेरे चित्तमें भी यही विचार स्थित है कि मैं उनका कोई अपराध नहीं करूँगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2357)
- **Original**: किन्तु आपने जो यह कहा कि “तुझे अनन्तसे क्या प्रयोजन है ?' सो ऐसी बातको भला कौन न्यायोचित कह सकता है ? आपका यह कथन किसी भी तरह ठीक नहीं है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2358)
- **Original**: ऐसा कहकर ये उनका गौरव रखनेके लिये चुप हो गये और फिर हैँसकर कहने लगे--“तुझे अनन्तसे क्या प्रयोजन है ? इस विचारकों घन्यवाद है !
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2359)
- **Original**: हे मेरे गुरुणण ! आप कहते हैं कि तुझे अनन्तसे क्या प्रयोजन है ? धन्यवाद है आपके इस लिचास्कों ! अच्छा, यदि आपको युरा न लगे तो मुझे अननन्‍्तसे जो प्रयोजन है सो सुनिये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2360)
- **Original**: धर्ष, अर्थ काम और मोक्ष--ये चार पुरुषार्थ कहे जाते हैं। ये चारों ही जिनसे सिद्ध होते हैं, उनसे क्‍या प्रयोजन 27-- आपके इस कथनको क्या कहा जाय !
- **Translation**: 

---

