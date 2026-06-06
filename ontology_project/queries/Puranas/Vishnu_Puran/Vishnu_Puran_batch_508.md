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

### Verse 1 (Vishnu Puran 0.10141)
- **Original**: श्रीपराशर्जी खोल्ले--तदनन्तर. अक्र्रजी, श्रोकृष्णचन्द्र और बलरामजी सम्पूर्ण गोपोंकों केंसको आज्ञा सुना नन्‍्दगोपके घर सो गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10142)
- **Original**: दूरोरे दिन निर्मल प्रभातकाल होते ही महातेजस्वी राम और कष्णक्पर अक्रूरके साथ मथुरा चलनेकी तैयारी करते देख जिनकी भुजाओंके कंकण ढीले हो गये हैं वे गोपियाँ नेत्रोंसें आँसू भरकर तथा दुःखार्त होकर दीर्घ निउ्चास छोडती हुई परस्पर कहने लूगों---
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10143)
- **Original**: “अब मधथुरापुरो जाकर श्रोकृष्णचन्द्र फिर गोकुलमें क्‍यों आने लगे ? क्योंकि यहाँ तो ये अपने कामनोंसे नगरनारियोंके मधुर आल्लापरूप मधुका ही पान करेंगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10144)
- **Original**: अः98ध)। विल्लासवाक्यपानेषु नागरीणां कृतास्पदम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10145)
- **Original**: चित्तमस्थ कथ्थ॑ भूयो ग्राम्यगोपीषु यास्यति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10146)
- **Original**: । 15 सार॑ सम्रस्तगोष्टस्य विधिना हरता हरिम्‌। अ्रहते गोपयोषित्सु निर्घुणेन दुरात्मना
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10147)
- **Original**: 16 भावगर्भस्मितं बाक्यं बिलासललिता गति: । नागरीणामतीबैतत्कटाक्षेक्षितमेव. च्
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10148)
- **Original**: 17 गआम्यो हरिस्यं तासां विलासनिगड़ैर्युत: । भवतीनां पुनः पाश्वै कया युकत्या समेष्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10149)
- **Original**: 18 एणैष रथमारुद्म मधुरां याति केशबः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10150)
- **Original**: क्ररेणाक्ररकेणात्र निर्घणेन प्रतारितः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10151)
- **Original**: 19 कि न वेत्ति नृशसोउयमनुरागपरं जनम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10152)
- **Original**: येनैवमक्ष्णोरा्वादं नयत्यन्यत्र नो हरिम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10153)
- **Original**: 20 एप रामेण सहितः प्रयात्यत्यन्तनिर्धण: । रथमारुद्य गोविन्दस्त्वर्यतामस्थ खारणे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10154)
- **Original**: 29 गुरूणामग्रतो वक्तु कि ब्रवीषिन न: क्षमम्‌ । गुरव: कि करिष्यन्ति दग्धानां विरहाओिना
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10155)
- **Original**: 22 नन्‍्दगोपमुखा गोपा गन्तुमेते समुद्यता:। नोदाम॑ कुरुते कश्रिद्रोविन्दविनिवर्तने
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10156)
- **Original**: 23 सुप्रभाताद्य रजनी मथुरावासियोषिताम्‌। पास्यन्त्यच्युतवक्‍त्राब्ज यासां नेत्रालिपड्रूय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10157)
- **Original**: 24 धन्यास्ते पश्चि ये कृष्णमितो यान्त्यनिवारिता: । उद्दहिष्यन्ति पह्यन्तस्स्वदेहं पुछकाश्लितम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10158)
- **Original**: 25 को नु ख्वप्नस्सभाग्याभिर्दृष्टस्ताभिरधो क्षजम्‌ । विस्तारिकान्तिनयना या द्रक्ष्यन्यनिवारिता:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10159)
- **Original**: 27 अहो गोपीजनस्यास्य दर्शयित्वा महानिधिम्‌ । उल्कृत्तान्यद्य नेत्राणि विधिनाकरुणात्मना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10160)
- **Original**: 28 अनुरागेण शैथिल्यमस्मासु त्रजिते हरों। जैथिल्यमुपयान्त्याशु करेषु बलयान्यपि
- **Translation**: 

---

