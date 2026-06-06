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

### Verse 1 (Vaivtpuran 18.18655)
- **Original**: शयानों.. रलपर्यड्ले रलभूषणभूषितः । रत्नभूषणभूषाड़ो.. राधावक्षसि. संस्थित:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.18656)
- **Original**: चन्दनोक्षितसर्वाड्र: स्मेराननसरोरुहः । प्रोद्यत्प्रेमरसाम्भोधौ निमग्र: सतत सुखातू
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.18657)
- **Original**: मल्लिकामालतीमालाजालै:_ शोभितशेखर: । पारिजातप्रसूनानां गन्धामोदितमानस:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.18658)
- **Original**: पुंस्कोकिलकलध्यानैर्ध्रमरध्वनिसंयुते: । कुसुमेषू _विकारेण पुलकाड्डितविग्रहः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.18659)
- **Original**: प्रियाप्रदत्तताम्बूलं भुक्तवानू यः सदा मुदा । बेदा अशक्ता य॑ स्तोतुं जडीभूता विचक्षणा:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.18660)
- **Original**: तमनिर्वचनीयं च कि स्तौमि नागवाजल़भा । वन्देहँ ल्वत्पदाम्भोज॑ ब्रहोशशेषसेवितम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.6840)
- **Original**: झ34 * संक्षिप्त ग्रह्मवैवर्तपुराण * #%##%##ऋ#ऋ#%##ऋ#ऋ%#%ऋऋकऋ कक # 64 #######%#%#4%$%%%%%% 8 ##### #क्ककऋऋऋ%ऋऋ$%%#######%##%% तीनों काल इसका पाठ करता है, वह समस्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.6841)
- **Original**: और उसे सम्पूर्ण तीर्थोंमें ्लान करनेका फल प्राप्त व्याधियोंसे मुक्त हो जाता है। उसके अंधापन,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.6842)
- **Original**: होता है--इसमें तनिक भी संदेह नहीं है। अतः कोढ़, दरिद्रता, रोग, शोक, भय और कलह--ये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.6843)
- **Original**: पुत्रो! तुमलोग शीघ्र ही पुष्करमें जाओ और वहाँ सभी विश्वेश्वर श्रीसूर्यकी कृपासे निश्चय ही नष्ट
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.6844)
- **Original**: सूर्यका भजन करो। यों कहकर ब्रह्मा आनन्दपूर्वक हो जाते हैं। जो भयंकर कुषप्ठसे दुःखी, गलित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.6845)
- **Original**: अपने भवनको चले गये। इधर बे दोनों दैत्य अन्ञोंवाला, नेत्रहीन, बड़े-बड़े घावोंसे युक्त, सूर्यकी सेवा करके नौरोग हो गये। बत्स नारद! यक्ष्मासे ग्रस्त, महान्‌ शूलरोगसे पीड़ित अथवा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.6846)
- **Original**: इस प्रकार मैंने तुम्हारे पूछे हुए विश्नेश्वरके नाना प्रकारकी व्याधियोंसे युक्त हो, वह भी यदि
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.6847)
- **Original**: विप्नका कारण तथा सर्वविष्नहर सूर्यकवच और एक मासतक हविष्यात्र भोजन करके इस स्तोत्रका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.6848)
- **Original**: सूर्यस्तवादि सुना दिये। अब तुम्हारी और क्‍या श्रवण करे तो निश्चय ही रोगमुक्त हो जाता है
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.6849)
- **Original**: सुननेकी इच्छा है? (अध्याय 19) #328504 जल फ/ं-++प++ भगवान्‌ नारायणके निवेदित पुष्पकी अवहेलनासे इन्द्रका श्रीभ्रष्ट होना, पुनः बृहस्पतिके साथ ब्रह्माके पास जाना, ब्रह्माद्वारा दिये गये नारायणस्तोत्र, कवच और मन्त्रके जपसे पुनः श्री प्राप्त करना तब श्रीनारायणने कहा--नारद! एक बार
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.6850)
- **Original**: महालक्ष्मी छायाकी तरह सदा उसके साथ रहेगी। देवराज इन्द्र निर्जन वनमें, एक पुष्पोद्यानमें गये [वह ज्ञान, तेज, बुद्धि, बल--सभी बातोंमें सब थे। वहाँ रम्भा अप्सरासे उनका समागम हुआ।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.6851)
- **Original**: देवताओंसे श्रेष्ठ और भगवान्‌ हरिके तुल्य तदनन्तर वे दोनों जलविहार करने लगे। इसी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.6852)
- **Original**: पराक्रमी होगा। परंतु जो पामर अहंकारबश बीच मुनिश्रेष्ठ दुर्वासा बैकुण्ठसे कैलास जाते हुए
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.6853)
- **Original**: भगवान्‌ श्रीहरिके निवेदित इस पुष्पकों मस्तकपर शिष्यमण्डलीसहित वहाँ आ पहुँचे। देवराज इन्द्रने
- **Translation**: 

---

