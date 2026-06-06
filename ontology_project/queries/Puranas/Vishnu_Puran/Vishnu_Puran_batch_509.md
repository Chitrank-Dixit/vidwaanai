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

### Verse 1 (Vishnu Puran 0.10161)
- **Original**: 29 पक्कप अंदर ह- 3000 नगरकी [ विदग्घ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10162)
- **Original**: बनिताओंके विलासयुक्त बचनोंके रसपानमें आसक्त होकर फिर इनका चित्त गैंवारी गोपियोंकी ओर क्यों जाने लगा ?
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10163)
- **Original**: आज निर्दयी दुरात्पा विधाताने समस्त वजके सारभूत (सर्वस्वस्वरूप) श्रीहरिको हस्कर हम गोपनारियॉपर घोर आघात किया है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10164)
- **Original**: नगरकी नारियोंमें भावपूर्ण मुसकानमयों बोली, विल्लसल्लित गति और कराक्षापूर्ण चितबनकी स्वभावसे ही अधिकता होती है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10165)
- **Original**: उनके विलास-बन्धनोंसे बैंधकर यह ग्राम्य हरि फिर किस युक्तिसे तुम्हारे [ हमारे ] पास आलेगा ?
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10166)
- **Original**: देखो, देखो, क्रूर एवं निर्दयी अक्रूरके बहकानेमें आकर ये कृष्णचन्द्र रघपर चढ़े हए मथुरा जा रहे हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10167)
- **Original**: यह नुशंस अक्रूर क्या अनुरागीजनोंके हदयका भाव तनिक भो नहीं जानता ? जो यह इस प्रकार हमारे नयनानन्दवर्धन नन्‍्दनन्दनको अन्यत्र लिये जाता है.
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10168)
- **Original**: देखो, यह अत्यन्त निलवर गोविन्द रामके साथ रथपर चढ़कर जा रहे हैं; अरी ! इन्हें ग्रेकनेमें शीघता कये'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10169)
- **Original**: [ इसपर गुरुजनोंके सामने ऐसा करनेमें असमर्थता प्रकट करनेयाज्जी किसी गोपीक्ो लक्ष्य करके उसने फिर कहा-- ] “अरी ! तू क्‍या कह रहो है कि अपने गुरुजनॉके सामने हम ऐसा नहीं कर सकतीं ?'' भल्त्र अब चिस्टाग्रिसे भस्मीभूत हुई हमत्त्रेगॉंका गुरुजन क्‍या करेंगे ?
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10170)
- **Original**: देखो, यह नन्‍दगोप आदि गोपगण भी उन्हींके साथ जानेको तैयारी कर रहे हैं। इनमेंसे भी कोई गोबिन्दको छौटानेका प्रयत्न नहीं करता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10171)
- **Original**: आजकी रात्रि सथुरावासिनो स्वियोंके लिये सुन्दर प्रभातयाल्जी हुई है, क्योंकि आज उनके नयन-पभंग श्रीअच्युत्के मुखारखविन्दका मकरनद पान करेंगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10172)
- **Original**: जो लोग इधररों बिना गेक्त-टोक श्रोकृष्णचद्धका अनुगमन कर रहे है वे धन्य हैं, क्योंकि थे उनका दर्शन करते हुए अपने गोमाहझयुक्त जारीरका बहन कऋेरेंगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10173)
- **Original**: 'आज अश्रीगोविन्दके अंग-प्रत्यंगॉंको देखकर मधुरायासियोंके नेश्नॉफो अत्यन्त महोत्सव होगा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10174)
- **Original**: आज न जाने उन भाग्य- शालिनियोनि ऐसा कौन शुभ स्वप्त देखा है जो वे कान्तिपय विशाल नयनॉवाली (मथुरापुणीक्त्रे स्त्रयाँ) स्वच्छन्दता पूर्वक श्रीअधोक्षजकों निहारेंगी ?
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10175)
- **Original**: अहो ! गिष्ठर विधाताने गोपियोंकों महानिधि दिखलाकर आज उनके नेत्र निकल लिये
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10176)
- **Original**: देखो ! हमारे प्रति श्रीहरिके अनुशगमें शिथिकतता आ जानेसे हमारे हाथोंके कंकण भी तुरंत ही ढीले पड़ गये हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10177)
- **Original**: 358 अक्वूरः क्ररहदयइशीघ्र॑ प्रेरयते हयान्‌। एबमार्त्तासु योषित्सु कृपा कस्य न जायते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10178)
- **Original**: 30 एप कृष्णरथस्ोचैश्षक्ररेणुरनिरीक्ष्यताम्‌ । दूरीभूतो हरियेंन सो5पि रेणुर्न लक्ष्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10179)
- **Original**: 31 अ्ीप्राज़र उबाच डत्येबमतिहादैन गोपीजननिरीक्षित: । तत्याज ब्रजभूभागं सह रामेण केझव:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10180)
- **Original**: 32 गच्छन्तो जवनाश्वेन रथेन यमुनातटम्‌। ज्राप्ता मध्याह्समये रामाक़ूरजनार्दनाः
- **Translation**: 

---

