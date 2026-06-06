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

### Verse 1 (Vishnu Puran 0.12081)
- **Original**: 51 स्वल्पाम्बुवृष्टि: पर्जन्य: सस्‍्ये स्वल्पफले तथा । फल॑ तथाल्पसार॑ च विप्र प्राप्ते कल युगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12082)
- **Original**: 52 झाणीप्रायाणि वस्लाणि झमीप्राया महीरुहा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12083)
- **Original**: शृद्र॒प्रायास्तथा वर्णा भविष्यन्ति कौ युगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12084)
- **Original**: 53 अणुप्रायाणि धान्यानि अजाप्राय॑ तथा पय: । भविष्यति कल्मो प्राप्ते छौशीरं चानुलेपनम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12085)
- **Original**: 54 श्वश्ूश्रशुरभूयिष्ठा गुरवक्ष नृ्णां कलौ। इयालाद्या हारिभार्याश्व सहदो मुनिसत्तम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12086)
- **Original**: 55 कस्य माता पिता कस्ब यथा कर्मानुग: पुमान्‌ इति चओदाहरिष्यन्ति श्वशुरानुगता नरा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12087)
- **Original**: 56 कलिमें पाँच-छ़: अथवा सात वर्षकी खो और आठ- नौ या दस वर्षके पुरुषोंके ही सनन्‍्तान हो जायगी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12088)
- **Original**: बारह यर्षकी अवस्थामें ही छोगोंके बाल पकने कगेंगे और कोई भी व्यक्ति बीस बर्षसे अधिक जीवित न रहेगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12089)
- **Original**: कलियुगमें लोग मन्द-बुद्धि, व्यर्थ चिह्न धारण करनेवाले और दुष्ट चित्तवाले होंगे, इसलिये वे अल्पकालमें ही नष्ट हो जायैंगे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12090)
- **Original**: हे मैत्रेय ! जब-जब धर्मकी अधिक हानि दिखलायी दे तभी-तभी बुद्धिमान्‌ मनुष्यकों कलियुगकी बुद्धिका अनुमान करना याहिये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12091)
- **Original**: हे मैत्रेय ! जब-जब पाषण्ड बढ़ा हुआ दीखे तभी-तभी महात्माओंको कल्युगकी बद्धि समझनी चाहिये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12092)
- **Original**: जब- जब वैदिक मार्गका अनुसरण करनेजाले सत्पुरुषोंका अभाव हो तभी-तभी बुद्धिमान्‌ मनुष्य कलिकी वृद्धि हुई जाने
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12093)
- **Original**: हे मैत्रेय ! जब धर्मात्मा पुरुषोंके आरम्भ किये हुए कार्योमें असफलता हो तत्र पष्डितजन कलियुगकी प्रधानता समझें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12094)
- **Original**: जब-जब यज्ञॉंके अधीश्वर भगवान्‌ पुरुषोत्तमका स्म्रेग यज्ञोंट्रारा यजन न करें. तब-तब कल्का प्रभाव ही समझना चाहिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12095)
- **Original**: जब वेद-बादमें प्रीतिका अभाव हो और पाषण्डमें प्रेम हो तब बुद्धिमान प्राज्ञ पुरुष कलियुगकों बढ़ा हुआ जानें
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12096)
- **Original**: हे मैत्रेय ! कलियुगमें लोग पाषण्डके वश्शौभूत हो जानेसे सबके रचयिता और प्रभु जगत्पति भगवान्‌ विष्णुका पूजन नहीं करेंगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12097)
- **Original**: हे विष्र ! उस समय लोग पाषण्डके बशीभूत होकर कहेंगे--इन देव, द्विज, वेद और जलसे होनेवाले शौचादिमें क्या रखा है?'
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12098)
- **Original**: हे विप्र ! कलिके आनेपर वृष्टि अल्प जलवाल्ी होगी, खेती थोड़ी उपजबाली होगी और 'फत्शदि अल्प सास्युक्त होंगे। 52
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12099)
- **Original**: कलियुगमें प्रायः सनके बने हुए सबके वख होंगे, अधिकतर दामीके वक्ष होंगे और चार्रो वर्ण बहुधा शुद्ववत्‌ हो जायैंगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12100)
- **Original**: कलिके आनेपर धान्य अत्यन्त अणु होंगे, प्राय: बकरियोंका ही दूध मिलेगा और उशीर (खस) ही एकमात्र अनुल्ेपन होगा
- **Translation**: 

---

