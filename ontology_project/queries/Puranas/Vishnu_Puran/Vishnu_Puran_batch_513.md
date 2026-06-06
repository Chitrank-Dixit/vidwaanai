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

### Verse 1 (Vishnu Puran 0.10241)
- **Original**: मानते हुए यमुनाजलसे निकलकर फिर रथके पास दरदर्श रामकृष्णां च यथापूर्वभवस्थितो चले आये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10242)
- **Original**: वहाँ आकर उन्होंने आश्चर्ययुक्त नेत्रोंसे ते अब । राम और कृष्णको पूर्ववत्‌ रथमें बैठे देख्खा । उस समय विस्मिताक्षस्तदाक़ूरस्तं च कृष्णोभ्यभाषत
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10243)
- **Original**: क्रीकृष्णचद्धने अक्रूरजीसे कहा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10244)
- **Original**: कृष्ण उताच श्रीकृष्णजी योल्े--अक्रूरजों ! आपने अवश्य हो त्ते यमुनाजले । यमुन्ा-जलमें कोई आश्चर्यजनक बात देखी है, क्योंकि नून॑ ते दृष्टमा यमुना विस्मयोत्फुल्लनयनो यत:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10245)
- **Original**: आपके नेत्र आश्चर्ययकित दीख पड़ते है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10246)
- **Original**: अक्ूूर उकाच अन्तर्जले यदाक्षर्य दृष्ट तत्र मयाच्युत । तदत्रापि हि पश्यामि मूर्तिमत्पुरतः स्थितम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10247)
- **Original**: जगदेतन्महाश्चर्यरूप॑ यस्थ॒ महात्मन:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10248)
- **Original**: त्ेनाश्चर्यपरेणाई भवता कृष्ण सद्भत्त:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10249)
- **Original**: तत्किमेतेन मथुरां यास्थामों मधुसूदन। बिभेपि कंसाद्धिग्जन्म परपिण्डोपजीविनाम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10250)
- **Original**: इत्युक्सवा चोदयामास स हयान्‌ वातरंहस: । सम्प्राप्तआपि सायाद्े सो क्रूरो मथुरां पुरीम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10251)
- **Original**: अक्वरजी बोल्ठै--हे अच्युत ! मैंने यमुनाजलमें जो आश्चर्य देखा है उसे मैं इस समय भी अपने सामने मूर्तिमान्‌ देख रहा हूँ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10252)
- **Original**: हे कृष्ण ! यह महान्‌ आश्चर्यमय जगत्‌ जिस महात्पाका स्वरूप है उन्हीं परम आश्चर्यस्वरूप आपके साथ मेरा समागम हुआ है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10253)
- **Original**: है मधुसदन ! अब उस आश्षर्यके विषयमें और अधिक कहनेसे स्ताभ ही क्‍या है ? चलो, हमें शीघ्र ही मथुरा पहुँचना है; मुझे कँससे यहुत भय छगता है। दूसरेके दिये हुए अन्नसे जीनेयाले पुरुषोंके जीवनको घिक्कार है !
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10254)
- **Original**: ऐसा कहकर अक्रूरजीने वायुके समान वेगवाले घोड़ोंको हॉँका और सायड्रालके समय मथुरापुरोमें पहुँच
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10255)
- **Original**: आअ* 19 ] विल््रेक्य मथुरा कृष्ण रामं चाह स यादव: । पद्भ्यां यात॑ महावीरौ रथेनैको विज्ञाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10256)
- **Original**: 10 गन्तव्यं बसुदेबस्य नो भवद्भ्यां तथा गृहम्‌। युवयोहिं कृते वृद्धस्स कंसेन निरस्यते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10257)
- **Original**: 19 श्रीपराशर उच्च इत्युक्त्वा प्रबिवेशाथ सो5क्रूरो मथुरा पुरीम्‌ । प्रविष्टी रामकृष्णा च राजमार्गमुपागतों
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10258)
- **Original**: 12 खीभिनरेश्व सानन्‍्द॑ लोचनैरभिवीक्षितो । जम्मतुलीलया वीरो मत्तो बालगजाबिव
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10259)
- **Original**: 13 भ्रममाणो ततो दृष्ठा रजक॑ रड्डकारकम्‌। अयाचेतां सुरूपाणि बासांसि रुचिराणि तौ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10260)
- **Original**: 94 कंसस्थ रजकः सो5थ प्रसादारूढबिस्मय: । बहुन्याक्षेपवाक्यानि प्राहोच्चै रामकेशवौ
- **Translation**: 

---

