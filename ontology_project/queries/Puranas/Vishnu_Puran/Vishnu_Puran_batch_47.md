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

### Verse 1 (Vishnu Puran 0.921)
- **Original**: 65 अऑपराशर उवाच एवं संस्तूयमानस्तु भगवाउ्छद्धचक्रधृक्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.922)
- **Original**: जगाम दर्शन तेषां मैत्रेय परमेश्वर:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.923)
- **Original**: 66 ते दृष्ा ते त़दा देखाः शजद्भुचक्रगदाधरम्‌ । अपूर्वरूपसंस्थान॑ तेजसां राज्चिमूर्जितम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.924)
- **Original**: 67 भ्रणम्व प्रणताः सर्वे संक्षोभस्तिमितेक्षणा: । तुष्ुवु: पुण्डरीकाक्ष॑ पितामहपुरोगमा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.925)
- **Original**: 68 देवा ऊचुः नमो नमो5विशेषस्त्व त्वे ब्रह्मा त्वं पिनाकधृक्‌ । इन््रस्त्वभशि: पवनो वरुण: सब्ति यम:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.926)
- **Original**: 69 बसबो मरुतः साध्या विश्वेदेवणणा: भवान्‌ । यो5र्व _तवाग्रतो देव समीप॑ देवतागण: । स त्वम्ेय जगर्स्त्रष्टा यत: सर्वगतो भवान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.927)
- **Original**: 70 त्वं यज्ञस्त्वं बषद्कारस्त्वमोद्ूररः प्रजापति: । विज्ञा वेचां च सर्वात्म॑स्त्वत्मयं चाखिल जगत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.928)
- **Original**: 71 त्वामार्त्ता: झरणं किष्णो प्रयाता दैत्यनिर्जिता: । ब्य प्रसीद सर्वात्मिस्तेजसाप्याययस्व नः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.929)
- **Original**: 72 तावदार्त्तिस्तथा वाब्छा तावन्मोहस्तथाउसुखम्‌ । यात्रन्न याति झरणं त्वामझेषाघनाशनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.930)
- **Original**: 73 त् प्रसाद प्रसन्नात्मन्‌ प्रपन्नानां कुरुष् नः । तेजसां नाथ सर्वेधां स्वशकक्‍्त्याप्याय्न कुरु
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.931)
- **Original**: 74 अधथम अंग हेड सर्वगत अच्युत ! जिसे ये भगकान्‌ ब्रह्माजी भी नहीं जानते, आपके उस परमपदको हम प्रणाम करते हैं!
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.932)
- **Original**: तदनन्तर ब्रह्मा और देवगणोंके बोल चुकनेपर बृहस्पत्ति आदि समस्त देवर्षिगण कहने ल्गो--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.933)
- **Original**: “जो परम स्तवनीय आइ्य यज्ञ-पुरुष हैं और पूर्वजोंके भी पूर्वपुल्ष हैं उन जगत्के रचयिता निर्विशेष परमात्माको हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.934)
- **Original**: हे भूत-भन्येश यज्ञमूर्तिधर भगवन्‌ ! है अव्यय
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.935)
- **Original**: हम सब दारणागतोपर आप प्रसन्न डोइये और दर्शन दीजिये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.936)
- **Original**: हे नाथ ! हमारे सहित ये ब्रद्माजी, रद्रोंके सहित भगवान्‌ शंकर, बारहों आदित्योंके सहित भगवान्‌ पूषा, अग्नियोंके सहित पावक और ये दोनों अश्विनीकुमार, आठों वसु, समस्त मरुद्रण, साध्यगण, बिश्वेदेव तथा देबराज इनद्ध ये सभी देवगण दैत्य-सेनासे पराजित होकर अति प्रणत हो आपकी झरणमें आये है!
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.937)
- **Original**: 69--65
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.938)
- **Original**: श्रीपराशरजी खोस्छे--हे मैत्रेय ! इस प्रकार स्तुति किये जानेपर हसन चक्रधारी भगवान्‌ परमेश्वर उनके सम्मुख प्रकट हुए
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.939)
- **Original**: तब उस इख-चक्रगदाधारी उत्कृष्ट तेजोराशिमय अपूर्व दिव्य मूर्तिको देखकर पितामह आदि समस्त देवगण अति विनयपूर्वक प्रणामकर क्षोेभवश चकित-नयन हो उन कमलनयन भगवान्‌की स्तुति करने लगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.940)
- **Original**: देवगण बोले--हे प्रभो ! आपको नमस्कार है, नमस्कार है। आप निर्विशेष हैं तथापि आप हो ब्रह्मा हैं, आप ही शंकर हैं तथा आप ही इन्द्र, अभ्रि, पतन, वरुण, सूर्य और यमराज हैं
- **Translation**: 

---

