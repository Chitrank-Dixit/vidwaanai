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

### Verse 1 (Narsihma Puran 0.4661)
- **Original**: 157-19
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.4662)
- **Original**: नृषबर! इस प्रकार यह परमपुरुष भगवान्‌ विष्णुकी पूजा-बिधि आज भैंने तुम्हें बतायो है। यदि तुम्हें वैष्णव- पद प्राप्त करतेकी इच्छा हो तो इस विधिके द्वारा सदा प्राप्तु तदिष्टे यदि वैष्णव पदम्‌
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.4663)
- **Original**: भगवान्‌ विष्णुकौ पूजा करो
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.4664)
- **Original**: इति ऑकफासिहएराणे विग्णोरचाविधिनाम ट्विग्टितिमोउ ध्याय: 662
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.4665)
- **Original**: / इस प्रकार ऑनयमिंहग॒गणयें '
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.4666)
- **Original**: षवाप्‌ विश्युकी पूका-विधि नामक वासठवाँ अध्याप बूरा हुआ # 62
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.4667)
- **Original**: हे अष्टाक्षर-मन्चके प्रभावसे इद्धका स्त्रीयोनिसे उद्धार सफस्तानीक उवाच सत्यपुक्त त्वया ब्रह्मन्‌ वैदिक: परमो विधि: । विष्णोर्देयातिदेवस्थ पूजन प्रति मेउथुना
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.4668)
- **Original**: 1 अनेन विधिना ब्रह्मन्‌ पूज्यते मथुसूदन: सहस्वानीक बोले--ब्राह्मतू! इस समय आपने देवदेवेश्वर भगवान्‌ विष्णुके पूजतकी यह उत्तम बैदिक विधि यतायी, वह बिलकुल ठौक है; परंतु ब्रह्मन्‌। इस विधिसे तो केवल जेदज्ञ पुरुष ही मधुसूदतकी पूजा कर सकते हैं, दूसरे लोग नहीं; इसलिये आप ऐसी कोई वेदज़ैरैव नान्यैस्तु तस्मात्सर्वह्चित॑ वद
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.4669)
- **Original**: जिधि बताइये, जो सबके लिये उपयोगी हों
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.4670)
- **Original**: अध्याय 63 ] क्रीमार्कण्ड्रेथ उकाच अष्टाक्षेण . देवेशं नरसिंहमनामयम्‌। गन्थपुष्पादिभिरनित्यमर्चयेदच्युतं नर:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.4671)
- **Original**: 3 राजन्रष्टाक्षो मज्र: सर्वपापहर: परः। समस्तयज्ञफलद: सर्वशान्तिकर: शुभ:
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.4672)
- **Original**: 4 30 नमो नारायणाय। गन्धपुष्पादिसकलमनेनैव निवेदयेत्‌। अनेनाभ्यर्थितो देव: प्रीतो भवति तत्क्षणात्‌
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.4673)
- **Original**: 5 किं तस्य बहुभिम॑न््रै: कि तस्य बहुभित्तते:। 3* नमो नारायणायेति मन्त्र: सर्वार्थााथक:
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.4674)
- **Original**: 6 डुमं मन्त्र जपेहास्तु शुत्रिर्भूत्ता समाहितः। सर्वपापव्िनिर्मुक्तो विष्णुसायुज्यमाप्रुयात्‌
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.4675)
- **Original**: 7 सर्वतीर्थपलं॑ होतत्‌ सर्वतीर्थवर॑ नृप। हरेरचंनमव्यग्रं सर्ववज्ञफल॑ नृप
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.4676)
- **Original**: 8 तस्मात्कुरू नृपश्रेष्ठ प्रतिमादिषु चार्चनम्‌। दानानि यिप्रमुखेभ्य: प्रयच्छ बिधिना नृप। एवं कृते नृपश्रेष्ठ नरसिंहप्रसादत:। प्राप्रोति वैष्णय तेजो यत्काडक्षन्ति मुपुक्षब:
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.4677)
- **Original**: 9 पुरा पुरंदरों राजन्‌ स्त्रीत्य॑ प्राप्तोउपधर्मत:। तृणविन्दुमुने: शापान्युक्तो हाष्टाक्षराज्पात्‌
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.4678)
- **Original**: 10 सहसर्वीक उवाच एतत्कथय भूदेव देवेन्धस्याधमोचनम्‌। को5पथर्म: कर्थ॑ स्त्रीत्वे प्राप्ते मे बद कारणम्‌
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.4679)
- **Original**: 11 अीयाकण्डेय उवाच राजेद्ध महदाख्यानं श्रुणु कौतूहलान्वितम्‌। विष्णुभक्तिप्रजननं॑ थृण्वतां पठतामिदम्‌
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.4680)
- **Original**: 12 पुरा पुरंदरस्यैव देवराज्यं प्रकुर्वतः। बैराग्यस्थापि जनन॑ सम्भूत॑ जाह्मवस्तुषु
- **Translation**: 

---

