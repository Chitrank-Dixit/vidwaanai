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

### Verse 1 (Vaivtpuran 13.10482)
- **Original**: सब गोपबालक हँसने, नाचने और खुशीसे गीत हो श्रीकृष्णको आशीर्वाद देने लगे। इसी बीचमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10483)
- **Original**: गाने लगे। प्रलम्बासुरका वध करके बलरामसहित श्रीकृष्ण ब्रह्मतेजसे प्रज्वलित हो उठे। उन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10484)
- **Original**: परमेश्वर श्रीकृष्ण शीघ्र ही गोचारणके कार्यमें परमेश्वरने बाहर और भीतरसे दैत्यके सारे अज्जोंमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10485)
- **Original**: जुट गये। वे गौएँ चराते हुए भाण्डीरवनके पास दाह उत्पन्न कर दिया। तब उन सबका वमन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10486)
- **Original**: जा पहुँचे। करके उस दानवने प्राण त्याग दिये। उस समय माधवकों जाते देख बलवान्‌ इस प्रकार बकासुरका वध करके बलवान दैत्यराज केशीने अपनी टापसे धरतीकों खोदते श्रीकृष्ण ग्वालबालों और गौओंके साथ अत्यन्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10487)
- **Original**: हुए शीघ्र ही इन्हें घेर लिया। उसने श्रीहरिको मनोहर केलि-कदम्ब-काननमें जा पहुँचे। इसी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10488)
- **Original**: मस्तकपर चढ़ाकर संतुष्ट हो आकाशमें सौ समय वहाँ वृषरूपधारी प्रलम्ब नामक असुर आ
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10489)
- **Original**: योजनतक उन्हें उछाल-उछालकर घुमाया और पहुँचा, जो बड़ा बलवान, महान्‌ धूर्त तथा।अन्तमें पृथ्वीपर गिर पड़ा। उस पापीने श्रीहरिके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10490)
- **Original**: 90 क्र संक्षिप्त ब्रह्मवैवर्तपुराण ] कक ऋऋ्ककऋफऋऋऋ ## 6 ###
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10491)
- **Original**: ###ऋऊऋऊऋऊऋऊऋऋ 4 #########%#%%% 5555 % ## # हाथको दाँतसे पकड़ लिया और क्रोधपूर्वक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10492)
- **Original**: पुरुष आये, जो श्रीहरिको प्रणाम करके उनकी चबाना आरम्भ किया। परंतु श्रीहरिके अज्ग वज्रके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10493)
- **Original**: स्तुति करते हुए उसी विमानसे उत्तम गोलोकको समान कठोर थे। उनके अड्भका चर्बण करते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10494)
- **Original**: चले गये। वे तीनों पहलेके वैष्णव पुरुष थे, ही दैत्यके सारे दाँत टूट गये। श्रीकृष्णके तेजसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10495)
- **Original**: जो देह त्यागकर दानबी योनिको प्राप्त हुए थे। दग्ध होकर उसने भूतलपर प्राणोंका परित्याग कर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10496)
- **Original**: वे ही इस समय श्रीकृष्णके हाथों मारे जाकर दिया। स्वर्गमें दुन्दुभियाँ बजने लगीं और वहाँ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10497)
- **Original**: उनके पार्षद हो गये। फूलॉंकी वर्षा आरम्भ हो गयी। इसी बीचमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10498)
- **Original**: . नारदजीने पूछा--महाभाग ! वे दिव्य वैष्णव पुरुष कौन थे, जो दैत्यरूप हो गये थे? इस बातको बताइये। यह कैसी परम अद्भुत बात सुननेको मिली है? भगवान्‌ नारायण बोले--ब्रह्मन्‌! सुनो। मैं इसका प्राचीन इतिहास बता रहा हूँ। मैने पुष्करतीर्थमें सूर्यग्रहणके अवसरपर साक्षात्‌ महेश्वरके मुखसे इस विषयको सुना था। श्रीहरिके गुण- 4 88 है.
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10499)
- **Original**: कोर्ततके प्रसड़में भगवान्‌ शंकरने यह कथा कही ; 6 &
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10500)
- **Original**: थी। गन्धमादन पर्वतपर गन्धर्वराज गन्धवाह रहा "
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10501)
- **Original**: करते थे। वे श्रीहरिकी सेवामें तत्पर रहनेबाले महान्‌ तपस्वी और श्रेष्ठ संत थे। मुने! उनके चार है
- **Translation**: 

---

