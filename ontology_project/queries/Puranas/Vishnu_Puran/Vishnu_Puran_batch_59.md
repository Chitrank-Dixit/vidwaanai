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

### Verse 1 (Vishnu Puran 0.1161)
- **Original**: 13 शपराशर उकाय इत्युक्त: सकल मात्रे कथयामास तद्ाथा । सुरुचि: प्राह भूपालघ्रत्यक्षमतिगर्विता
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1162)
- **Original**: 14 बिनिःश्वस्पेति कथिते तस्मिन्पुत्रेण दुर्मना: । श्रासक्षामेक्षणा दीना सुनीतिर्वाक्यमग्रवीत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1163)
- **Original**: 15 सुनीतिरुवाच सुरुचि: सत्यमाहेदं मन्दभाग्यो5सि पुत्रक । न हि पुण्यवतां वत्स सपल्रेरेबमुच्यते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1164)
- **Original**: 16 नोद्वेगस्तात कर्त्तव्यः कृत यद्धवता पुरा । तत्को5पहर्तु शक़ोति दातुं कश्षाकृ्त त्वया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1165)
- **Original**: 17 तत्त्वया नात्र कर्त्तव्यं दु:ख॑ तद्बाक्यसप्यवम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1166)
- **Original**: 18 बैठनेकी हुई
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1167)
- **Original**: किन्तु राजाने अपनी प्रेयसी सुरुचिके सामने, गोदपें चढ़नेके लिये उत्कण्ठित होकर प्रेमबश आये हुए उस पुत्रका आदर नहीं किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1168)
- **Original**: अपनी सौतके पुत्रको गोदमें चढ़नेके लिये उत्सुक और अपने पुत्रको गोदमें बैडा देख सुरुचि इस प्रकार कहने लूगणी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1169)
- **Original**: “अरे छल्ला ! ब्रिना मेरे पेटसे उत्पन्न हुए किसी अन्य स्त्रोका पुत्र होकर भी तू व्यर्थ क्‍यों ऐसा बड़ा मनोरथ करता है ?
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1170)
- **Original**: तू अविवेकी है, इसीलिये ऐसी अलभ्य उत्तमोत्तम वस्तुकी इच्छा करता है। यह ठीक है कि तू भी इन्हों राजाका पुत्र है, तथापि मैंने तो तुझे अपने गर्भपें धारण नहीं क्रिया!
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1171)
- **Original**: सपस्त चक्रलती राजाओंका आश्रयरूप यह राजपिंडासन तो मेरे ही पुत्रके योग्य है; तू व्यर्थ क्यों अपने चित्तको सन्ताप देता है?
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1172)
- **Original**: मेरे पुत्रके समान तुझे लृथा हो यह ऊँचा मनोरथ क्यों होता है ? क्या तू नहीं जानता कि तेरा जन्म सुनीतिसे हुआ है ?''
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1173)
- **Original**: अआपराइरजी बोल्ले--हे द्विज ! विमाताका ऐसा कथन सुन वह बालक कुपित हो पिताको छोड़कर अपनी माताके महलकों चल दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1174)
- **Original**: हे मैत्रेय ! जिसके ओघ् कुछ-कुछ काँप रहे थे ऐसे अपने पुत्रक्यो क्रोधयुक्त देख सुनीतिने उसे गोदमें बिठाकर पूछा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1175)
- **Original**: ''बेटा ! तेरे क्रोधका कया कारण है ? तेरा किसने आदर नहों किया ? तेरा अपराध करके कौन तेरे पिताजीका अपमान करने चत्य है 2?”
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1176)
- **Original**: ओपराशरजी ओले--ऐसा पूछनेपर धुवने अपनी मातासे थे सब बातें कह दीं जो अति गर्बॉली सुरुचिने उससे पिताके सामने कही थीं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1177)
- **Original**: अपने पुत्रके सिसक- सिसककर ऐसा कहनेपर दु:खिनी सुनौतिने स्तिन्न चित्त और दीर्घ निःधासके कारण मलिननयना होकर कहा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1178)
- **Original**: सुनीति बोली--बेटा ! सुरुचिने झौक ही कहा है, अवदय ही तू मन्दभाग्य है। हे वत्स ! पृण्यवानोंसे उनके बिपक्षों ऐसा नहीं कह सकते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1179)
- **Original**: बच्चा ! तू व्याकुल मत हो, क्योंकि तूने पूर्-जन्मोंमें जो कुछ किया है ठसे दूर कौन कर सकता है ? और जो नहीं किया वह तुझे दे भी कौन सकता हैः? इसलिये तुझे उसके वाक्योंसे खेद
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1180)
- **Original**: डर राजासनं॑ राजत्तजत्र॑ वराश्चवरवारणा: । यस्य पुण्यानि तस्यैते मत्वैतच्छाम्य पुत्रक
- **Translation**: 

---

