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

### Verse 1 (Vaivtpuran 13.11462)
- **Original**: होती है, सम्पूर्ण ब्रत-उपवास, सब तपस्या, प्रभाव श्रुतिमें दुर्लभ है। उनके चरणकमलोंकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11463)
- **Original**: महादान तथा श्रीहरिकी आराधना करनेपर जो धूलिसे पृथ्वी तत्काल पवित्र हो जाती है। उनका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11464)
- **Original**: पुण्य सुलभ होता है, सम्पूर्ण पृथ्वीकी परिक्रमा, जो चरणचिह्न है, उसीको तीर्थ कहा गया है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11465)
- **Original**: सम्पूर्ण वेदवाक्योंके स्वाध्याय तथा समस्त यज्ञोंकी उनके स्पर्शमात्रसे तीर्थॉंका पाप नष्ट हो जाता है।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11466)
- **Original**: दीक्षा ग्रहण करनेपर मनुष्य जिस पुण्यको पाता उनके आलिडुन, श्रेष्ठ वार्तालाप, दर्शन और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11467)
- **Original**: है; वही पुण्य बुद्धिमान मानव गौओंकों घास स्पर्शसे भी मनुष्य समस्त पापोंसे छुटकारा पा देकर पा लेता है*। जाता है। सम्पूर्ण तीथॉमें भ्रमण और स्नान करनेसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11468)
- **Original**: . जो घास चरती हुई गायको स्वेच्छापूर्वक *तीर्थस्रानेध.. यत्पुण्य॑ यत्पुण्य॑ विप्रभोजने। सर्वव्रतोपवासेषु. सर्वेष्वेव. तपःसु. च
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11469)
- **Original**: यत्पुण्य॑ च महादाने. यत्पुण्य॑ हरिसेवने। भुव: पर्यटने यत्तु वेदवाक्येषु यद्धभवेत्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11470)
- **Original**: यत्पुण्य॑ सर्वयज्ञेपु. दीक्षायां च लभेन्नर:। तत्पुण्यं लभते प्राज्शों गोभ्यो दत््वा तृणानि च
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11471)
- **Original**: (215। 87-89)
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11472)
- **Original**: चरनेसे रोकता है, उसे ब्रह्महत्याका पाप लगता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11473)
- **Original**: नन्दजीकी यह बात सुनकर बलरामसहित है तथा वह प्रायश्षित्त करनेपर ही शुद्ध होता श्रीकृष्ण जोर-जोरसे हँसने लगे और पुनः है। पिताजी! सब देवता गौओंके अन्जोंमें, सम्पूर्ण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11474)
- **Original**: प्रसन्नतापूर्वक पितासे बोले। तीर्थ गौओंके पैरोंमें तथा स्वयं लक्ष्मी उनके गुदा श्रीकृष्णने कहा--तात! आज मैंने आपके स्थानों (मल-मूत्रके स्थानों)-में सदा वास करती
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11475)
- **Original**: मुखसे बड़ी विचित्र और अद्भुत बात सुनी है। हैं। जो मुनष्य गायके पद-चिहसे युक्त मिट्टीद्वारा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11476)
- **Original**: इसका कहीं भी निरूपण नहीं किया गया है तिलक करता है, उसे तत्काल तीर्थस्नानका फल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11477)
- **Original**: कि इन्द्रसे वृष्टि होती है। आज आपके मुखसे मिलता है और पग-पगपर उसकी विजय होती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11478)
- **Original**: अपूर्व नीतिवचन सुननेको मिला है। सूर्यसे जल है। गौएँ जहाँ भी रहती हैं, उस स्थानको तीर्थ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11479)
- **Original**: उत्पन्न होता है और जलसे शस्य एवं वृक्ष उत्पन्न कहा गया है। वहाँ प्राणोंका त्याग करके मनुष्य
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11480)
- **Original**: होते और बढ़ते हैं। उनसे अन्न और फल पैदा तत्काल मुक्त हो जाता है, इसमें संशय नहीं है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11481)
- **Original**: होते हैं तथा उन अन्नों और फलॉसे जीवधारी जो नराधम ब्राह्मणों तथा गौओंके शरीरपर प्रहार
- **Translation**: 

---

