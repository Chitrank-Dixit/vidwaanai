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

### Verse 1 (Vishnu Puran 0.1441)
- **Original**: 86 अन्येषां दुर्लभ स्थान॑ कुले स्वायम्भुवस्य यत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1442)
- **Original**: . 87 तस्वैतदपरं बाल येनाह॑ परितोषितः । मामाराध्य नरो मुक्तिमवाप्रोत्यविलम्बिताम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1443)
- **Original**: । 88 मस्वर्षितमना बाल किमु स्वर्गादिकं पदम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1444)
- **Original**: 89 तैस्थ्रेक्यादधिके स्थाने सर्वताराग्रहाश्रय: । भ्रविष्यति न सन्देहों मत्मसादाद्धवाद्युव
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1445)
- **Original**: 90 सूर्यात्सोमात्तथा भौमात्सोमपुत्रादबृहस्पते: । सितार्कतनयादीनां सर्वक्षाणां तथा ध्रुब
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1446)
- **Original**: 99 सप्तर्षीणापशेषाणां ये च वैमानिका: सुरा: । सर्वेषामुपरि स्थार्न तब दत्त मया घरुब
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1447)
- **Original**: 92 केचिशवतुर्युगं यावत्केचिन्मन्वन्तरें सुरा; । तिष्ठन्ति भवतो दत्ता मया वै कल्पसंस्थिति:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1448)
- **Original**: 93 सुनीतिरपि ते माता त्वदासब्नातिनिर्मला । वबिमाने तारका भूत्वा तावत्कालं निवत्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1449)
- **Original**: 94 येच त्वां मानवा: प्रात: सायं च सुसमाहिता: । कीर्त्तयिष्यन्ति तेषां च महत्युण्यं भविष्यति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1450)
- **Original**: 95 भ्रीपराशर उवाच एवं पूर्व जगन्नाथाह्देवदेवाज्जनार्दनात्‌ । बरं प्राप्य ध्रुव: स्थानमध्यास्ते स महापते । 96 स्वयं शुअ्रूषणाद्धम्यात्मातापित्रोश्व वै तथा । दादशाक्षरमाहात्म्यात्तपसश्र॒ प्रभावत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1451)
- **Original**: 97 तस्याभिमानमृद्धि चर महिसान॑ निरीक्ष्य हि । देबासुराणामाचार्य: इल्लोकमत्रोशना जगौ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1452)
- **Original**: 98 अश्लेषस्य तपसो वीर्यमहोउस्थ तपस: फलम्‌ । यदेन॑ पुरतः कृत्वा ध्रुबं सप्तर्षयः स्थिता:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1453)
- **Original**: 99 धुबस्प जननी चेयय॑ सुनीतिरनाथ सूनृता । प्रथम अंश श्र] 2 &£&4 &4 तग्रथअंश हु 9 देखकर तेरी ऐसी इच्छा हुई कि 'मैं भी राजपुत्र होऊँ/
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1454)
- **Original**: अतः हे घुब ! तुझको अपनी मनोवाजिछत राजपुषरता प्राप्त हुई और जिन स्वायम्पुबमनुके कुछूमें और किसीको स्थान मिल्तना अति दुर्लभ है, उन्हींके घरमें दूने उत्तानपादके यहाँ जन्म लिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1455)
- **Original**: अरे बालक ! [ औरेंके लिये यह स्थान कितना ही दुर्कभ हो परन्तु ] ज्सने मुद्दे सन्तुष्ट किया है उसके लिये तो यह अत्यन्त तुच्छ है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1456)
- **Original**: मेरी आराधना करनेसे तो मोक्षपद भी तत्काल प्राप्त हो सकता है, फिर जिसका चित्त निरत्तर मुझमें ही लगा हुआ है उसके लिये स्वर्गादि लोकॉका तो कहना ही क्‍या है ?
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1457)
- **Original**: हे ध्रुव ! मेरी कपासे तू निस्सन्देह उस स्थानमें, जो त्रिल्लेकीमें सबसे उत्कृष्ट है, सम्पूर्ण ग्रह और तारामप्डलका आश्रय बनेगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1458)
- **Original**: हे घ्लूव ! मैं तुझे वह धुत (निश्चल) स्थान देता हूँ जो सूर्य मंगल, बुध, बहस्पति, शुक्र और शनि आदि ग्रहों, सभी नक्षत्रों, सप्र्चियों और सम्पूर्ण विमानचारी देवगणोंसे ऊपर है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1459)
- **Original**: देवताओमेंसे कोई तो केवल चार युगतक और कोई एक मन्वन्तरतक ही रहते हैं; किन्तु तुझे मैं एक कल्पतककी स्थिति देता हूँ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1460)
- **Original**: तेरी माता सुनीति भी अति स्वच्छ तारारूपसे उतने ही समयतक तेरे पास एक विमानपर नितास करेगी
- **Translation**: 

---

