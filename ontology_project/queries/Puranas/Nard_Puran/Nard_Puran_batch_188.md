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

### Verse 1 (Nard Puran 224.3741)
- **Original**: कल्याण हो। अब मैं अमित तेजस्वी व्यासजीके 'महापुराणका श्रवण करके धन, रत्न और बन्त्र
- **Translation**: 

---

### Verse 2 (Nard Puran 224.3742)
- **Original**: समीप जाऊँगा। आदिके द्वारा भक्तिभावसे पुराणवाचक आचार्यकी
- **Translation**: 

---

### Verse 3 (Nard Puran 224.3743)
- **Original**: _ ऐसा कहकर सूतजी शौनक आदि महात्माओंसे पूजा करनी चाहिये। भूमिदान, गोदान, रत्रदान तथा
- **Translation**: 

---

### Verse 4 (Nard Puran 224.3744)
- **Original**: पूजित हो उन सबकी आज्ञा लेकर चले गये। वे हाथी, घोड़े और रथके दानसे आचार्यको सदैव संतुष्ट
- **Translation**: 

---

### Verse 5 (Nard Puran 224.3745)
- **Original**: शौनक आदि द्विज श्रेष्ठ महात्मा भी जो यज्ञानुष्ठानमें करना चाहिये। ब्राह्मणो! यह पुराण धर्मका संग्रह
- **Translation**: 

---

### Verse 6 (Nard Puran 224.3746)
- **Original**: लगे हुए थे, एकाग्रचित्त हो सुने हुए समस्त करनेवाला तथा धर्म, अर्थ, काम और मोक्ष-चारों
- **Translation**: 

---

### Verse 7 (Nard Puran 224.3747)
- **Original**: धर्मोके अनुष्ठानमें तत्पर हो, बहीं रहने लगे। जो पुरुषार्थोंको देनेवाला है। जो इसको व्याख्या करता है,
- **Translation**: 

---

### Verse 8 (Nard Puran 224.3748)
- **Original**: कलिके पाप-विषका नाश करनेवाले श्रीहरिके उसके समान मनुष्योंका गुरु दूसरा कौन हो सकता है।
- **Translation**: 

---

### Verse 9 (Nard Puran 224.3749)
- **Original**: जप और पूजन-विधिरूप औषधका सेवन करता शरीर, मन, बाणी और धन आदिके द्वारा सदा
- **Translation**: 

---

### Verse 10 (Nard Puran 224.3750)
- **Original**: है, वह निर्मल चित्तसे भगवान्‌के ध्यानमें लगकर धर्मोपदेशक गुरुका प्रिय करना चाहिये। इस पुराणको
- **Translation**: 

---

### Verse 11 (Nard Puran 224.3751)
- **Original**: सदा मनोवाज्छित लोक प्राप्त करता है। (0.ल्‍>>
- **Translation**: 

---

### Verse 12 (Nard Puran 224.3752)
- **Original**: पूर्वभाग समाप्त
- **Translation**: 

---

### Verse 13 (Nard Puran 224.3753)
- **Original**: ली जओ 24,000
- **Translation**: 

---

### Verse 14 (Nard Puran 224.3754)
- **Original**: निवलिआर नमः श्रीगणेशाय नमः 3 नमो भगवते वासुदेवाय श्रीनारदम्‌हापुराण उत्तरभाग महर्षि वसिष्ठका मान्धाताको एकादशीब्रतकी महिमा सुनाना पान्तु वो जलदश्यामा: शार्ड्ज्याघातकर्कशा:
- **Translation**: 

---

### Verse 15 (Nard Puran 224.3755)
- **Original**: गया है। वह भूत, वर्तमान अथवा भविष्य कैसा अैलोक्यमण्डपस्तम्भाश्वत्वारो हरिबाहव:
- **Translation**: 

---

### Verse 16 (Nard Puran 224.3756)
- **Original**: ही क्‍यों न हो, किस अग्रिसे दग्ध हो सकता है? 'जो मेघके समान श्यामवर्ण हैं, शार्ड्रधनुषकी
- **Translation**: 

---

### Verse 17 (Nard Puran 224.3757)
- **Original**: यह जानना मुझे अभीष्ट है। प्रत्यज्वाके आघात (रगड़)-से कठोर हो गयी हैं तथा त्रिभुवनरूपी विशाल भवनकों खड़े रखनेके लिये मानो खंभेके समान हैं, भगवान्‌ विष्णुकी वे चारों भुजाएँ आप लोगोंकी रक्षा करें।' सुरासुरशिरोरत्रनिषृष्टमणिरक्चितम्‌ । हरिपादाम्बुजद्वन्द्रमभीष्टप्रदमस्तु न:
- **Translation**: 

---

### Verse 18 (Nard Puran 224.3758)
- **Original**: *भ्रगवान्‌ श्रीहरिके वे युगल चरणारविन्द हमारे अभीष्ट मनोरथोंकी पूर्ति करें, जो देवताओं
- **Translation**: 

---

### Verse 19 (Nard Puran 224.3759)
- **Original**: और असुरोंके मस्तकपर स्थित रत्नमय मुकुटकी
- **Translation**: 

---

### Verse 20 (Nard Puran 224.3760)
- **Original**: ! घिसी हुई मणियोंसे सदा अनुरक्ञित रहते हैं।' मान्धाताने ( वसिष्ठजीसे ) पूछा-द्विजोत्तम ! जो भयंकर पापरूपी सूखे या गीले ईंधनको जला सके, ऐसी अग्नि कौन है? यह बतानेकी कृपा करें। ब्रह्मपुत्र! विप्र-शिरोमणे! तीनों लोकोंमें
- **Translation**: 

---

