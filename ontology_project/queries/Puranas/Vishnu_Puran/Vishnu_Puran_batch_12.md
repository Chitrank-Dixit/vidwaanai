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

### Verse 1 (Vishnu Puran 0.221)
- **Original**: तेन तस्थ निबोध लत परिमाणोषपादनम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.222)
- **Original**: 6 अन्येषां चैब जत्तूनां चराणामचराश्न ये। भूभूभूत्सागरादीनामहोषाणां च सत्तम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.223)
- **Original**: 7 काष्ठा पदश्लदशाख्याता निमेषा मुनिसत्तम
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.224)
- **Original**: काष्टा ब्रिंशत्कल्ल त्रिंझत्कला मौहूर्तिको विधि:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.225)
- **Original**: 8 तावत्संख्यैरहोरात्र मुहूर्सैर्मानु्ष॑ स्पृतम्‌। अह्ोरात्राणि ताबन्ति मास: पक्षद्दयात्यक:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.226)
- **Original**: 9 ते: घड़भिरयन वर्ष द्वेष्यने दक्षिणोत्तरे। अयने दक्षिणं राज्रिदेबानामुत्तरं दिनम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.227)
- **Original**: 10 दिव्यर्वर्पसहस्नैस्तु. कृतप्रेतादिसंज्ञितम्‌ । चतुर्युग॑ द्वादशभिस्तद्विभागं निदोध में
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.228)
- **Original**: 11 चत्वारि त्रीणि है चैक कृतादिषु यथाक्रमम्‌ । दिव्याब्दानां सहस्नाणि युगेघ्वाहु: पुराविद:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.229)
- **Original**: 12 तत्प्रमाणै: शत: सम्ध्या पूर्वा तत्राभिधीयते । सन्ध्यांशा्षैय तत्तुल्यो युगस्थानन्तरो हि स:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.230)
- **Original**: 13 सन्ध्यासन्ध्यांज्योरन्तर्य: कालो मुनिसत्तम । युगाख्य: स तु विज्ञेयः कृतत्रेतादिसंज्ञित:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.231)
- **Original**: 14 कृतं त्रेता द्वाप॑क्ष कलिश्रैय चतुर्युगम्‌। प्रोच्यते तत्सहस््नं च ब्रह्मणो दिवस मुने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.232)
- **Original**: 15 ब्रह्यणो दिवसे ब्रह्मश्मनवस्तु चतुर्दश । भ्रवन्ति परिमाणं च तेषां कालकृतं श्रृणु
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.233)
- **Original**: 16 सप्तर्षयः सुरा: शक्रो मनुस्तत्सूनवो नूपा: । एककाले हि सृज्यन्ते संडियन्ते च पूर्ववत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.234)
- **Original**: 97 श्रीपराश्ारजी छोले--हे तपस्बिियोंमें श्रेष्ठ मैत्रेय ! समस्त भाव-पदार्थोंकी झक्तियाँ अचिन्त्य-ज्ञानकी विषय होतो है; [उनमें कोई युक्ति काम नहीं देती] अत्तः अप्निको शक्ति उष्णताके समान ब्रह्मकी भी सर्गादि- रचनारूप दाक्तियाँ स्वाभाविक हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.235)
- **Original**: अब जिस प्रकार नारायण नापक स्मेक-पितामह भगवान्‌ ब्रह्माजी सृष्टिकी रचनामें प्रवृत्त होते हैं सो सुनो। है विद्वन्‌ू ! वे सदा उपचारसे हो 'उत्पन्न हुए' कहलाते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.236)
- **Original**: डनके अपने परिमाणसे डनकी आयु सौ वर्षकी कही जाती है। उस (सौ वर्ष) का नाम पर है, उसका आधा परार्ड कहल्लत्रता है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.237)
- **Original**: हे अनघ! मैंने जो तुप्से विष्णुभगवान्‌का कालस्वरूप कहा था उसीके द्वारा उस अह्माकी तथा और भी जो पृथिबी, पर्वत, समुद्र आदि चराचर जीव हैं उनकी आयुका परिमाण किया जाता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.238)
- **Original**: हे मुनिश्रेष्ठ ! फ्द्रह निमेषकों काष्ठा कहते हैं, तीस काष्ठटाकी एक कला तथा तीस कलाका एक मुहूर्त्त होता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.239)
- **Original**: तीस मुहूर्ततका मनुष्यका एक दिन-रात कहा जाता है और उतने ही दिन-रातका दो पक्षयुक्त एक मास होता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.240)
- **Original**: छः: महीनोंका एक अयन और दक्षिणायन तथा उत्तरायण दो अयन मिलकर एक वर्ष होता है। दक्षिणायन देवताओऑकी गात्रि है और उत्ततायण दिन
- **Translation**: 

---

