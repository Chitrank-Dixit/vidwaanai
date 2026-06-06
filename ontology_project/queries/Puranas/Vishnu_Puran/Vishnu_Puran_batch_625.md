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

### Verse 1 (Vishnu Puran 0.12481)
- **Original**: हे ट्विजश्रेष्ठ ! केवल नरकमें ही दुःख हों, सो बात नहीं है, स्वर्गमें भी पतनका भय रूगे रहनेसे कभी शान्ति नहीं मिलती
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12482)
- **Original**: [ नरक अथवा स्वर्ग-भोगके अनन्तर ] जार-बार वह गर्भमें आता है और जन्प ग्रहण करता है तथा फिर कभी गर्भमें ही नष्ट हो जाता है और कभो जन्म लेते ही मर जाता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12483)
- **Original**: जो उत्पन्न हुआ है वह जन्मते हो, बराल्यावस्थामें, युवावस्थामें, मध्यमवयमें अथवा जगराग्रस्त ह्ोनेपर अवश्य मर जाता हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12484)
- **Original**: जबतक जीता है तबतक नाना प्रकारके कष्टोंसे घिरा रहता है, जिस तरह कि कपासका बोज तन्‍्तुओंके कारण सूत्रोंसे घिरा रहता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12485)
- **Original**: द्रव्यके उपार्जन, रक्षण और नाझमें तथा इष्ट-मित्रोंके विपत्तिग्रस्त होनेपर भी मनुष्योंकों अनेकों दुःख उठाने पड़ते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12486)
- **Original**: हे मैत्रेय ! मनुष्योंको जो-जो वस्तुएँ प्रिय हैं, वे सभी दुःखरूपी वृक्षका बोज हो जाती हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12487)
- **Original**: ख्ती, पुत्र, मित्र, अर्थ, गृह, क्षेत्र और धन आदिसे पुस्षोंकों जैसा दुःख होता है वैसा सुख नहीं होता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12488)
- **Original**: इस प्रकार सांसारिक दुःखरूप सूर्यके तापसे जिनका अन्तःकरण तप्त हो रहा है उन पुरुषोंको मोक्षरूपी वक्षकी [घनी] छायाको छोड़कर और कहाँ सुख मिल सकता है ?
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12489)
- **Original**: अत्तः मेरे मतमें गर्भ, जन्म और जरा आदि स्थानॉमें प्रकट होनेवाले आध्यात्मिकादि त्रिविध दुःख-समूहकी एकमात्र सनातन ओषधि भगवत्ाप्ति ही है जिसका निरतिश्ञय आननन्‍्दरूप सुझ्की प्राप्ति कराना ही प्रधान लक्षण है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12490)
- **Original**: इसलिये पण्डितजनॉंकों भगवत्माप्तिका प्रयत्न करना चाहिये । हे महामुने ! कर्म और ज्ञान--ये दो ही उसकी प्राप्तिके कारण कहे गये हैं। 60
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12491)
- **Original**: आ 5] षष्ठ अंश 449 पैजतसाममाव पा जा विद ना विवेकाश्च द्विधा ज्ञान पर॑ ब्रह्म विवेकजम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12492)
- **Original**: 61 अन्ध॑ तम इवाज्ञान दीपवच्चेन्रियोद्धवम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12493)
- **Original**: यथा सूर्यस्तथा ज्ञान यद्दिप्रषे विवेकजम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12494)
- **Original**: 62 मनुरष्याह बेदार्थ स्पृत्वा यन्मुनिसत्तम । सम्बन्धे गदतो मम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12495)
- **Original**: 63 डे ब्रह्मणी वेदितव्ये शब्दब्रह्म परं च यत्‌ । अब्दब्रह्मणि निष्णात: पर ब्रह्माथिगच्छति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12496)
- **Original**: 64 दे बै विद्ये वेदितव्ये इति चाथर्वणी श्रुतिः । परया ल्वक्षरप्राप्तिऋम्वेदादिमयापरा परया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12497)
- **Original**: 65 यत्तदव्यक्तमजरमचितन्त्यमजमव्ययम्‌ अनिर्देश्यमरूप॑ च पाणिपादाह्मसंयुतम्‌ ऐ 66 सर्वगत॑ नित्य॑ भूतयोनिरकारणम्‌ । व्याप्यव्याप्त यतः सर्व यह पहयन्ति सूरय:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12498)
- **Original**: 67 पियाबमालिल महम नक्िणों पा दम तत्परं धाम तद्धथेय॑ मोक्षकाड्लिभि: सक्षम : परम पदम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12499)
- **Original**: 68 तदेव॒भगवद्वाच्य॑ स्वरूप परमात्मन: । बाचको भगवषच्छब्दस्तस्याद्यस्याक्षयात्मन:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12500)
- **Original**: 69 एवं निगदितार्थस्य तत्तत््वे तस्य तक्तवतः । ज्ञायते येन तन्ज्ानं परमन्यल्रयीमयम्‌
- **Translation**: 

---

