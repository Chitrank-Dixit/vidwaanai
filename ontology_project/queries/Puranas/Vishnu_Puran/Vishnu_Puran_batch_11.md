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

### Verse 1 (Vishnu Puran 0.201)
- **Original**: 68 स एव सर्बभूतात्मा विश्वरूपो यतो5व्यय: । सर्गादिक तु तस्वैक भूतस्थमुपकारकम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.202)
- **Original**: 69 स एव सृज्य: स च सर्गकर्ता .. सए्वपात्यत्ति अपाल्यतेच
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.203)
- **Original**: ऋह्या होकर स्जोगुणका आश्रय लेकर इस संसारकी रचनामें प्रवृत होते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.204)
- **Original**: तथा रचना हो जानेपर सर्वगुण-चिशिष्ट अतुल पराक्रमी भगवान्‌ विष्णू डस्का कल्पान्तपर्यन्त युग-युगमें पाझ्न करते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.205)
- **Original**: हे मैत्रेय ! फिर कल्पका अन्त होनेपर अति दारूण तमः- प्रधात रुद्ररूप धारण कर ये जनार्दन विष्णु ही समस्त भूतोंका भक्षण कर लेते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.206)
- **Original**: इस प्रकार समस्त भूतोंका भक्षण कर संसारकों जल्मय करके ये परमेश्वर ओष-शस्यापर शायन करते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.207)
- **Original**: जगनेपर ज्रह्मारूप होकर ये फिर जगत्की रचना करते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.208)
- **Original**: बह एक हो भगवान्‌ जनार्दन जगत्‌की सृष्टि, स्थिति और संहारके लिये ब्रह्मा, विष्णु और शिव--इन तीन संज्ञाओंको घारण करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.209)
- **Original**: के प्रभु विष्णु सष्टा (क्ह्मा) होकर अपनी ही सृष्टि करते हैं, पालक किष्णु होकर पाल्यरूप व्मपना ही पालन करते हैं और अन्तमें स्वयं ही संहारक (हि) तथा स्वर्य ही उपसंहत (छीन) होते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.210)
- **Original**: 67, पृथियी, जल, तेज, वायु और आकाञ् तथा समस्त इच्धियाँ और अन्तःकरण आदि जितना जगत्‌ है सब है और क्योंकि वह अव्यय विष्णु ही विश्वरूप और सब सन भूतोंकि अत्तरात्मा हैं, इसरिक्ये ब्रह्मादि प्राणियोंमें स्थित सर्गादिक भी उन्हींके उपकारक हैं। [ अर्थात्‌ जिस प्रकार ऋत्विजोट्रारा किया हुआ हवन यजमानका उपकारक होता है, उसी तरह परमात्माके रचे हुए समस्त प्राणियोंद्वारा होनेवाली सृष्टि भी उन्हींकी उपकारक है ]
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.211)
- **Original**: ने सर्वस्वरूप, श्रेष्ठ, बरदायक और वरेण्य (प्रार्थनाके योग्य) भगवान्‌ ठिष्णु ही ब्रह्मा आदि अवस्थाओंद्वारा रचनेवाले है, ये ही रचे जाते हैं, वे हो पालते हैं, वे ही पाल्थित छोते हैं तथा वे ही संहार करते ब्रह्माद्मवस्थाभिरशेषमूतति-....... ........ विण्णुवरेष्रों बरदो बरेण्य:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.212)
- **Original**: हैं [और स्वय॑ ही संहत छोते हैं ]
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.213)
- **Original**: बन जी “नतततः इति श्रीविष्णुपुणाणे प्रथमें5शे द्वितीयो5घ्याय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.214)
- **Original**: आता औ 5++ तीसरा अध्याय ब्रह्मादिकी आयु और कारका स्वरूप औमेज्रेय उनाच निर्गुणस्याप्रमेयस्प. शुद्धस्याप्यमलात्मन: । श्रीमैश्रेयजी ओोले--हे भगवन्‌ ! जो ब्रह्म निर्गुण, अप्रमेय , हुद्ध और निर्मस्थत्पा है उसका सर्गादिका कर्ता कर्थ सर्गादिकर्तुत्व॑ ब्रह्मणो5भ्युपगाप्यते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.215)
- **Original**: होना कैसे सिद्ध हो सकता है 2?
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.216)
- **Original**: आ0 3 ] प्रथम अंञझ 9्‌ अीपराशर उवाच शक्तय: सर्वभावानामचिन्त्यज्ञानगोचरा: । यतोउतो ब्रह्मणस्तास्तु सर्गाद्या भावझक्तय: । भरवन्ति तपतां श्रेष्ठ पावकस्य यथोष्णता
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.217)
- **Original**: 2 तपन्नियोध यथा सर्गे भगवान्सम्प्रवर्तते । नारायणाख्यो भगवान्त्रह्मा छोकपितामह:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.218)
- **Original**: 3 उत्पन्न: प्रोच्यते विद्वत्नित्ममेवोपचारत:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.219)
- **Original**: 4 निजेन तस्य मानेन आबुर्वर्घशर्त स्मृतम्‌। तत्पराख्य तदरद्ध)॒ चर परार्मभिधीयते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.220)
- **Original**: 5 कालस्वरूप विष्णोश्व यन्ययोक्ते तवानध
- **Translation**: 

---

