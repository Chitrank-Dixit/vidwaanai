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

### Verse 1 (Vaivtpuran 18.1139)
- **Original**: पत्नीके साथ पुन: गन्धर्ब-नगरमें चला गया। सती भगवान्‌ श्रीकृष्ण अपनी शक्तियोंके साथ मालाबतीके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1140)
- **Original**: मालावतीने ब्राह्मणोंको करोड़ों रत्न और नाना पति--गन्धर्व उपबर्हणके शरीरमें अधिष्ठित हुए।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1141)
- **Original**: प्रकाके धन दिये तथा उन सबको भोजन उनका आबेश होते ही गन्धर्व वीणा लिये उठ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1142)
- **Original**: कराया। उनसे वेदपाठ और मड्गलकृत्य करबाये। बैठा और शीघ्र ही स्नानके पश्चात्‌ दो नवीन वस्त्र
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1143)
- **Original**: भाँति-भाँतिके बड़े-बड़े उत्सव रचाये। उन सबसमें धारण करके उसने देब-समूहकों तथा सामने खड़े
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1144)
- **Original**: एकमात्र हरिनामकीर्तनरूप मड्भलकृत्यकी प्रधानता हुए उन ब्राह्मणदेवताको प्रणाम किया। फिर तो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1145)
- **Original**: रही। देवता अपने-अपने स्थानकों चले गये और देवता दुन्दुभि बजाने और फूलोंकी वर्षा करने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1146)
- **Original**: ब्राह्मण-रूपधारी साक्षात्‌ श्रीहरि भी अपने धामको लगे। उन गन्धर्ब-दम्पतिपर दृष्टिपात करके उन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1147)
- **Original**: पधारे। शौनक! यह सब प्रसंग मैंने तुम्हें कह 0 02007 0080 27
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1148)
- **Original**: सुनाया। साथ ही स्तवराजका भी वर्णन किया। 2207
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1149)
- **Original**: जो वैष्णव पुरुष पूजाकालमें इस पुण्यमय स्तोत्रका चुनी 8.
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1150)
- **Original**: पाठ करता है, वह श्रीहरिकी भक्ति एवं उनके दास्यका सौभाग्य पा लेता है। जो आस्तिक पुरुष वर-प्राप्तिकी कामना रखकर उत्तम आस्था और भक्तिभावसे इस स्तोत्रको पढ़ता है, बह धर्म, “
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1151)
- **Original**: अर्थ, काम तथा मोक्ष-सम्बन्धी फलको निश्चय ही पाता है। इस स्तोत्रके पाठसे विद्यार्थीको विद्याका, धनार्थीको धनका, भार्याकी इच्छावालेको भार्याका -
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1152)
- **Original**: और पुत्रकी कामनावालेको पुत्रका लाभ होता है। «7»... धर्म चाहनेवाला धर्म और यशकी इच्छाबाला यश पाता है। जिसका राज्य छिन गया है, वह राज्य 2-2
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1153)
- **Original**: और जिसकी संतान नष्ट हो गयी है, बह संतान ः4
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1154)
- **Original**: पाता है। रोगी रोगसे और कैदी बन्धनसे मुक्त हो लक्ष्मीकान्त॑ पार्षदश्ल॒ सेवितं॑ च चतुर्भुजैः। कुत्रचित्‌ स्वांशरूपेण जगतां पालनाय च
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1155)
- **Original**: श्रेतद्दीपी विष्णुरूप॑ पद्मयया. परिसेवितम्‌ । कुत्रचित्‌ स्वांशकलया अब्रह्माण्डे ब्रह्मूपिणम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1156)
- **Original**: शिवस्वरूप॑ शिवदं स्वांशेन शिवरूपिणम्‌ । स्वात्ममः पषोड़शांशेत सर्वाधार परात्परमू
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1157)
- **Original**: स्वयं महद्विराइरूपं विश्वौध॑ यस्य लोमसु। लीलया स्वांशकलया जगतां पालनाय च
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1158)
- **Original**: नानावतार॑ विश्रन्त॑ बोौजं॑ तेषां सनातनम्‌ । वसन्तं कुत्रचित्‌ सन्त योगिनां हृदये सताम्‌
- **Translation**: 

---

