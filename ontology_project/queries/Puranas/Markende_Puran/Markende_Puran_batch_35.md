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

### Verse 1 (Markende Puran 0.681)
- **Original**: सम्पूर्ण लोकोंपर दवा करो, जिससे पहलेको भाँति भति हीं नारोका देवता जै। महाभागें! आज आप
- **Translation**: 

---

### Verse 2 (Markende Puran 0.682)
- **Original**: सूर्योदय हो। ये घरपर पधारी हैं। पुक्षत्ते अथबा मेरे इन ब्राह्मण्युवाब (तिदेलले आपको जो भी रू।यं हो. टसे बतानेको
- **Translation**: 

---

### Verse 3 (Markende Puran 0.683)
- **Original**: माण्डब्वेत प्रहाभागे शप्तो भर्ता ममेश्वरः। कृपा करें।
- **Translation**: 

---

### Verse 4 (Markende Puran 0.684)
- **Original**: युर्वोदये बिनाशं त्वे प्राफ्यसीत्यतिमन्युता
- **Translation**: 

---

### Verse 5 (Markende Puran 0.685)
- **Original**: अग्मूग्रेचाद ब्राह्मणीने कहा--महाभागै) साण्डव्य ऋषिने एते देवा: सहेद्रेण भामुपागम्य दुःखिता:।
- **Translation**: 

---

### Verse 6 (Markende Puran 0.686)
- **Original**: अत्यत्व क्रोधपें भरकर पेरे स्थामी-मेंरे इंश्रण्को शाप ज़्वड्ाक्यापास्तसत्कर्मदिनवक्तनिरूपणा:
- **Translation**: 

---

### Verse 7 (Markende Puran 0.687)
- **Original**: दिया है कि सूर्मेंदय होते हो तेरी मृत्यु हो जायगी। याचन्ते5हर्निशासंस्थां बधात्रदविखणिवताम्‌। अनसूबोबान अह तद्थ॑मायाता थ्रृणु चैतद्बचों मम
- **Translation**: 

---

### Verse 8 (Markende Puran 0.688)
- **Original**: थदि वा रोचते भद्ठे ततस्त्मद्चचनादहम
- **Translation**: 

---

### Verse 9 (Markende Puran 0.689)
- **Original**: । दिनाभायात्‌ समस्तानामभात्रो यायकर्मणाम्‌। करोमि पूर्वषरद्देह भर्तारं च नर्व॑ तब
- **Translation**: 

---

### Verse 10 (Markende Puran 0.690)
- **Original**: तदभाबात्‌ सुरा; पुष्टि नोपयाण्ति लपस्विति
- **Translation**: 

---

### Verse 11 (Markende Puran 0.691)
- **Original**: प्रया हि सर्वथा स्त्रीणां माहात्प्मं बरवर्णिति। अह्लनशैव॒ समुच्छेदादुचछेद; 'सर्वकर्पणाम्‌।
- **Translation**: 

---

### Verse 12 (Markende Puran 0.692)
- **Original**: पतिम्नतातामारॉध्यमितिं सम्मानवापि ते
- **Translation**: 

---

### Verse 13 (Markende Puran 0.693)
- **Original**: नदुच्छेदादनावृट्या. जगदुच्छेदमेप्यति
- **Translation**: 

---

### Verse 14 (Markende Puran 0.694)
- **Original**: अनसूवा बोलीं-- ऊल्याणी ! यदि तुम्हारों इच्छा तन्त्वमिक्कसि. चोदेतज्नगदुद्धरनुपापद:।
- **Translation**: 

---

### Verse 15 (Markende Puran 0.695)
- **Original**: हो और तुम कहो तो मैं तुम्हारे पतिको पूर्वनत्‌ प्रसीद साध्वि लोकानां पूर्वबद्वर्ततां पति:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.696)
- **Original**: । श्रोर एवं नयी स्वस्थ अग्रस्थाका कर दूँगो! >जाम्ल स्‍त्रौणां पृथानज्े गे आएं न्युगेय्लिय । भर्वशुक्र्वतैतानू शॉक्याॉटेटन्‌ व्रत हिंआ शस्नात्‌ झाध्यि गहाशा पतिशुद्रुषर्ण प्रति। न्मसा गति; सदा कार्या कतो चशे गतिः। अह्रले ध्यी यच्च पिजातेध्य: क़ुर्सद्ध्ताध्यर्ड4 सत्कियात: । तस्थाव्यर्द केवलाता्यचित्ता नारी भुझेः भृशुश्रूपपैय
- **Translation**: 

---

### Verse 17 (Markende Puran 0.697)
- **Original**: (16। 66063 वैस लव छह सहाभगे क्रताया सम भच्दिस्म
- **Translation**: 

---

### Verse 18 (Markende Puran 0.698)
- **Original**: आर्थाा झत्पया बतये शक्रा55र्येण्णप ढा छुपे 4 81%। 681
- **Translation**: 

---

### Verse 19 (Markende Puran 0.699)
- **Original**: +दत्तात्रेबजीके जन्म-प्रसड़में एक पतिव्रता श्राष्टणी तथा अनसूयाजीका चरित्र * 55 #-##& ##444 7 #14874
- **Translation**: 

---

### Verse 20 (Markende Puran 0.700)
- **Original**: 00747 कक 12144 7232 7522: %%5 .5:55:566:555। 65744 54 7 » # » 2206 4243
- **Translation**: 

---

