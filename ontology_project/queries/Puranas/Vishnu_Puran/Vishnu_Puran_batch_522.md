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

### Verse 1 (Vishnu Puran 0.10421)
- **Original**: [दूसरी>--] 'अरी ! क्या तुम नील्प्म्थर धारण किये इन दुग्ध, चन्द्र अथवा कमलनालके समान सुभ्रवर्ण बत्य्देवजीक्ों आते हुए नहीं देखती हो ?'”
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10422)
- **Original**: [तीसरी0--- ] ' अरी सस्लियो ! [ अखाड़ेमें] चकर देकर घूमनेवाले चाणूर और मुष्टिकके साथ क्रीडा करते हुए बलभद्र तथा कृष्णका हँसना देख स्तर ।''
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10423)
- **Original**: चौथी*--] हाय ! सस्क्ियो ! देखों तो चाणूरसे लड़तेके लिये ये हरि आगे बढ़ रहे हैं; क्या इन्हें छुड़ानेवाले कोई भी बड़े-यूढ़े यहाँ लहीं हैं?”
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10424)
- **Original**: “कहाँ तो यौखनमें प्रवेश करनेवाले सुकुमार-दारीर इयाम और कहाँ वजग़के समान कठोर दशारीस्वात्र यह महान्‌ असुर !
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10425)
- **Original**: ये दोनों नवयुयक तो बड़े ही सुकुमार दरीरवाले [ किंतु इनके प्रतिपक्षी ] ये चाणूर आदि दैत्य मलल अत्यन्त दारुण हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10426)
- **Original**: मल्लयुद्धके परी क्षकगर्णोंका यह बहुत बड़ा अन्याय है जो ये मध्यस्थ होकर भी इन बालक और बलबान्‌ मल्ल्मेंके युद्धकी उपेक्षा कर रहे हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10427)
- **Original**: भ्रीपराशरजी बोले--नगरकी स्तियोंके इस प्रकार बार्तालाप करते समय भगवान्‌ कृष्णचन्द्र अपनी कमर कसकर उन समस्त दर्सककि बीचमें पृथिवीको कम्पायमान करते हुए रह्न्धूमिपें कूद पड़े
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10428)
- **Original**: श्रीयरूभद्रजी भी अपमे भुजदप्ड्ोको ठोकते हुए अति मनोहर भावसे उछलने लगे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10429)
- **Original**: उस समय उनके पद-पदपर पृथिबी नहीं फटी, यही चड़ा आश्चर्य है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10430)
- **Original**: तदनत्तर अमित-चविक्रम कृष्णचच्द्र चाणूरके साथ और इन्द्रयुद्धकुल राश्षस मुष्टिक खलभद्रके साथ युद्ध करने लगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10431)
- **Original**: कृष्णचन्द्र चाणूरके साथ परस्पर भिड़कर,
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10432)
- **Original**: अबन् 20 ] पादोदधूत॑: प्रमृष्टेश तयोर्युद्धमभून्यहत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10433)
- **Original**: 67 अशस््रमतिधोर॑ तत्तयोर्युद्धं सुदारुणम्‌ । बलप्राणबिनिष्पादयं॑ समाजोत्सवसतन्निधौ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10434)
- **Original**: 68 यावद्यावध्ध चाणूरो युयुथे हरिणा सह। प्राणहानिमवापाग्रयां तावत्तावल्लवाल्लवम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10435)
- **Original**: 69 कृष्णो5पि युयुधे तेन लीलयैव जगन्पय: । खेदाघालयता कोपान्निजशेखरकेसरम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10436)
- **Original**: 70 बलक्षयं विवृद्धिं च दृध्ठा चाणूरकृष्णयो: । बारयामास तूर्याण कंसः कोपपरायण:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10437)
- **Original**: 71 मृदड्रादिषु तूर्येषु प्रतिषिद्धेषु तत्क्षणात्‌। खे सड्भतान्यवाद्यत्त देवतूर्याण्यनेकशः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10438)
- **Original**: 72 जय गोविन्द चाणूरं जहि केशव दानवम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10439)
- **Original**: अन्तर्द्धानगता. देबास्तमूचुरतिहर्षिता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10440)
- **Original**: 73 चाणूरेण चिरं काल क्रीडित्वा मधुसूदन: । उत्धाप्य भ्रामबामास तड्भ्राय कृतोद्यम:
- **Translation**: 

---

