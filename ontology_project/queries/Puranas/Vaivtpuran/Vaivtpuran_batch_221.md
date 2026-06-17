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

### Verse 1 (Vaivtpuran 13.10562)
- **Original**: पुरुष कलशपर, मणिमें, शालग्राम-शिलामें अथवा रूपके दर्शन कराये। उस रूपके दर्शन करके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10563)
- **Original**: जलमें राधासहित श्रीकृष्णका पूजन करे। पहले उन वैष्णवोंके नेत्रोंमें आँसू भर आये। वे सर्वरूपी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10564)
- **Original**: पाँच देवताओंकी पूजा करके भक्तिभावसे राधावललभ श्रीहरिको प्रणाम करके दानवी योनिमें चले गये।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10565)
- **Original**: श्रीकृष्णका ध्यान करे। उनके सामवेदोक्त ध्यानका इसलिये वे दानवेश्वर हुए। वसुदेव तो पहले ही
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10566)
- **Original**: वर्णन करता हूँ, सुनो। भगवान्‌ श्रीकृष्णकी मुक्त हो चुका था। सुहोत्र बकासुर, सुदर्शन अज्जकान्ति सजल जलधरके समान श्याम है। प्रलम्ब और स्वयं सुपार्श केशी हुआ था। भगवान्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10567)
- **Original**: वे रेशमी पीताम्बर धारण करते हैं। उनका मुख शेंकरके बरदानसे श्रीहरिके परम उत्तम रूपके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10568)
- **Original**: शरत्कालकी पूर्णिमाके चन्द्रमाके समान मनोहर दर्शन करके उन्हींके हाथसे मृत्युकों प्राप्त हो वे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10569)
- **Original**: है। उसपर मन्द हासकी प्रभा फैल रही है। नेत्र उनके परम धाममें चले गये। विप्रवर! श्रीहरिका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10570)
- **Original**: शरद्‌ ऋतुके प्रफुल्ल कमलोंकी शोभाको तिरस्कृत यह अद्भुत चरित्र कहा गया। बक, केशी और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10571)
- **Original**: कर रहे हैं। उनमें सुन्दर अज्ञन लगा हुआ है। प्रलम्बके उद्धारका यह प्रसड़ वाचकों और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10572)
- **Original**: वे गोपियोंके मनको बारंबार मोहते रहते हैं। राधा श्रोताओंकों मोक्ष प्रदान करनेवाला है।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10573)
- **Original**: उनकी ओर देख रही हैं। वे राधाके वक्ष:स्थलमें नारदजीने पूछा--महाभाग! आपके कृपा-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10574)
- **Original**: विराजमान हैं। ब्रह्मा, अनन्त, शिव और धर्म प्रसादसे यह सारी अद्भुत बात मैंने सुनी। अब
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10575)
- **Original**: आदि देवता उनको स्तुति करते हैं। _॒ 9फफऋफझफ$झ$ऊ5फपफप5फ"?ैीईी॑- फ/
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10576)
- **Original**: ट_ट_टत_क्‍पक्‍क्‍क्‍क्‍क्‍क्‍---- 1-ज्योतिषके अनुसार वह समय जब कि सूर्य विषुव रेखापर पहुँचता है और दिन-रात दोनों बराबर होते हैं।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10577)
- **Original**: * श्रीकृष्णजन्मखण्ड * 73 ू+44 4461 %$% 5546 #% 44466 #% # 5 4 15544 #£ ## ## ## 45 # 5 $ $ कक #/6# ## # ऋ इक #ऊ 4 # ऋ### # क. इस प्रकार श्रीकृष्णका ध्यान करके ब्रती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10578)
- **Original**: अड्जोंकी अपूर्व शोभा हो रही है। उत्तम रत्नोंके पुरुष उस ध्यानके द्वारा ही उनका सानन्द ' सारतत्वसे रचित मझौीरोंकी झनकारसे उनके दोनों आवाहन करे। इसके बाद बह राधाका ध्यान
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10579)
- **Original**: चरण सुशोभित होते हैं। ब्रह्मा आदिके भी करे। वह ध्यान यजुर्वेदकी माध्यन्दिनशाखामें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10580)
- **Original**: सेवनीय श्रीकृष्ण स्वयं ही उनकी सेवा करते वर्णित है। राधा रासेश्वरी हैं, रमणीया हैं और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10581)
- **Original**: हैं। सर्वेश्वके द्वारा उनकी स्तुति की जाती है ग्रसोललास-रसके लिये उत्सुक रहती हैं। रासमण्डलके
- **Translation**: 

---

