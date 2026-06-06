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

### Verse 1 (Markende Puran 0.1061)
- **Original**: प्रकार राजा भी प्रिय-अप्रिय तथा साधु और और सूर्य अपनी क्िरणोंका सर्वत्र सपान रूपसे
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1062)
- **Original**: दुएके प्रति रूमान भावसे राजनीतिका प्रयोग प्रसा/ करते हैं, उप्ती प्रकार तोतिके लिये
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1063)
- **Original**: करे। जैसे पूर्ण चन्द्रमा टेखकर सब मनुष्य प्रसन्न राजाकों भी समस्त प्रजापर सपान भाव रखना ; होते हैं, उसी प्रकार जिस राजाके प्रति समस्त चाहिये । वेश्या. कमल, शरभ, शुलिका, गर्भिणी
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1064)
- **Original**: प्रजाको समानरूपसे सन्तोष हो, बड़ी श्रेष्ठ एवं स्त्रोके सतत तथा ग्वालेको स्त्रीसे भी राजाको . चन्द्रमाके ब्रतका पालग करनेवाला है। जैसे वायु बुद्धि सीखनी चाँहिवे। राजा ज्लेश्शाको भाँते
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1065)
- **Original**: गुप्तूपसे समस्त प्रागियोंके भीतर सझ्ार करती सबको प्रसत्र ग्ख्नेकों चेष्टा करें, कमल -पुष्पके रहतो हैं, ठसी प्रकार राजा भी गुप्तचरके द्वारा समाभ सबकों अपनी ओर आकष्ट करें, शरभके
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1066)
- **Original**: पुरवासियों, मन्त्रियों तथा बन्धु-बान्धबोंके मतका स्तमान पशक्रमों बने, शूलिकाक्ती भाँति सहसा भाष जाननेकी चेष्टा करे।* शत्रुका विध्यंस करे। जैसे गर्भिणीके स्ततमें
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1067)
- **Original**: चेटा! जिसके चित्तकों दूसरे लोग लोभ, भावों सन्‍्तानके लिये दृधक्ता संप्रह होने लगता कामना अथबा अर्थसे नहीं खोंच सकते, वह है, उसो प्रकार राजा भविष्ठके लिये सक्षयशील
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1068)
- **Original**: राजा स्वर्गलोकमें जाता है। जो अपने धर्मसे बने और जिस प्रकार ग्वालेकी स्त्री दूधसे नागा
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1069)
- **Original**: बिचलित हो कुमार्गपर जानेवाले मूर्ख मनुष्योंको प्रकारके खाद्य पदार्थ तैयार करतों है, वैसे हो
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1070)
- **Original**: फिर धर्ममें लगाता है, वह राजा स्वर्गमें जाता राजाकों भी भाँति-भाँतिकी कल्पनामें पटु होना हैं। वत्स! जिसके राण्यमें वर्णध्मं और चाहिये। वह पृथ्वीका पालन करते समय एन्द्र,
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1071)
- **Original**: आध्रमधर्मकों हानि नहों पहुँचतो, उसे इस सूर्य, यम, सन्‍्द्रमा तथा वायु-इत पाँचोंके रूप लोक और गरलोकपें भी सनातन सुख प्राप्त धाराग करे। जैसे इन्द्र चार महीने वर्षा करके
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1072)
- **Original**: होता है। स्वयं दुष्टबुद्धि पुरुषोंद्रारा धर्मसे चृध्वीयर रहनंवाले प्राणिषोंकों तृप्त करते हैं, विचलित न होकर ऐसे लोगोंको अपने धर्ममें उसी प्रकार शजा दानके द्वारा प्रजाजनोंको सन्तुट्
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1073)
- **Original**: लगाना ही राजाका सबसे बड़ा कर्तव्य है और + ब्रेयािफिन्णलिकर्ता दौजणेस च शत्मले: । चद्स्‍सू॑स्वक्पेण तौत्ोें पृथितोशिता
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1074)
- **Original**: बस्धली -बाशर भशलिशार्गाचिणीज्वानात्‌ । प्रगा _ृपरेण चादैशा तथा गोफपलयोषितः
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1075)
- **Original**: इफ्ारकंदगस्पा्ण 766 चसोपंत्ीपति:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1076)
- **Original**: +पाणि पकू कुर्वोत महीगालनकर्मीण
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1077)
- **Original**: अधेचरआतुगे गाधार शेगोत्मरॉण धुशतम्‌ आध्यात्येलू लथा लोक परिक्ृरिमह्ीएति:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1078)
- **Original**: तथनएँ वथा सूर्ईस्तौय हरे रश्वि;। यृक्ष्पेणीणाष्युधानेश तथा शुल्फादिक तृष:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1079)
- **Original**: रुथः या. पिष्नेप्य! प्राशछाले नियच्छति
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1080)
- **Original**: तथा पिथाद्ियें राजा दुष्टादुे सी अबेत्‌
- **Translation**: 

---

