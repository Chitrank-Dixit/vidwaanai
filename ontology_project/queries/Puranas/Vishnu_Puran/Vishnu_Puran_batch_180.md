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

### Verse 1 (Vishnu Puran 0.3581)
- **Original**: जो भी पार्थिव वस्तु चरणसझ्ारके योग्य है वह भुलोक ही है। उसका विस्तार मैं कह चुका
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3582)
- **Original**: हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3583)
- **Original**: पृथिवी और सूर्यके मध्यमें जो सिद्धशएण और मुनिगण-सेबित स्थान है, जही दूसरा भुवल्लेंक है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3584)
- **Original**: सूर्य और धुतके बीचमें जो चौदह लक्ष योजनका अन्तर है, उसीको लोकस्थितिका विचार करनेवालोने स्वलॉक कहा है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3585)
- **Original**: हे मैत्रेय ! ये (भू:, धुबः, स्व:) 'कृतक' त्रैल्मेक्य कहलाते हैं और जन, तप तथा सत्य--ये तीनों 'अकृतक' लोक हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3586)
- **Original**: इन कृतक और अकृतक त्रिस्मेकियोंके मध्यमें महलोंक कहा जाता है, जो कल्पान्तमें केबल जनशूत्य हो जाता है, अत्यन्त नष्ट नहीं होता [इसलिये यह 'कृतकाकृत' कहलाता है]
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3587)
- **Original**: हे मैत्रेय ! इस प्रकार मैंने तुमसे ये सात लोक और सात ही पाताल कहे। इस ब्रह्माप्डका बस इतना ही बिस्तार बै
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3588)
- **Original**: यह ज़ह्माण्ड कपित्थ (कैये) के चीजके समान ऊपर-नीचे सब ओर अण्डकटाहसे घिरा हुआ है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3589)
- **Original**: हे मैत्रेय ! यह अप्ड अपनेसे दसगुने जलसे आबृत है और वह जल्का सम्पूर्ण आबरण अम्रिसे घिरा हुआ है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3590)
- **Original**: अप्रि वायुसे और वायु आकाइसे परिषेष्टित है तथा आकाद भूतोंके कारण तामस अहंकार और अहैकार महत्तत्वसे घिरा हुआ है। है मैत्रेय ! ये सातों उत्तरोत्तर एक-दूसरेसे दसणुने है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3591)
- **Original**: महत्तत््वको भी प्रधानने आवृत कर रखा है। वह अनन्त है; तथा उसका न कभी अन्त (नाश) होता है और न कोई संख्या ही है; क्‍योंकि हे मुने ! वह हेतुभूतमझेषस्थ प्रकृति: सा परा मुने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3592)
- **Original**: अनन्त, असंख्येय, अपस्मिय और सम्पूर्ण जगत्‌का अप्डानां तु सहस्नाणां सहल्लाण्ययुतानिच ।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3593)
- **Original**: कारण है और वहीं परा प्रकृति है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3594)
- **Original**: उसमें ईंदृशानां तथा तत्र कोटिकोटिशतानि च
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3595)
- **Original**: ऐसे-ऐसे हजारों, लाखों तथा सैकड़ों करोड़ ब्रह्माण्ड टासण्यरियथा तह शिके तद्पमानीय।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3596)
- **Original**: जिस प्रक्पर काष्ठमें अम्रि और तिरूमें तैल
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3597)
- **Original**: रहता है उसी प्रकार स्वप्रकाश चेतनात्मा व्यापक पुरुष प्रधानेउबस्थितो व्यापी चेतनात्मात्मबेदन:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3598)
- **Original**: ;थानमें स्थित है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3599)
- **Original**: हे महाबुद्धे ! ये संश्रयशील प्रधान च्व॒पुप्ांश्षेव्त सर्वभूतात्मभूतया । (आपसमें मिले हुए) प्रधान और पुरुष भी समस्त विष्णुशक्त्या महाबुद्धे वृतों संश्रवरधर्भिणौं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3600)
- **Original**: भूतोंको स्वरूपभूता विष्णु-शक्तिसे आवृत हैं
- **Translation**: 

---

