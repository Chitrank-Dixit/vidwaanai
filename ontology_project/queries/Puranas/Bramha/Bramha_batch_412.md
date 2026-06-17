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

### Verse 1 (Bramha 0.8221)
- **Original**: बार्तालाप, व्यर्थ भोजन और व्यर्थ धन द्विजोंके लिये जो-जो दुःखकी बात हो सकती है, वह
- **Translation**: 

---

### Verse 2 (Bramha 0.8222)
- **Original**: पतनके कारण होते हैं; इसलिये उन्हें सदा संयमी सब कलिकालमें होगी। संसारमें स्वाध्याय, वषट्कार,
- **Translation**: 

---

### Verse 3 (Bramha 0.8223)
- **Original**: रहना आवश्यक है। यदि वे सभी वस्तुओंमें स्वधा और स्वाहाका शब्द नहीं सुनायी देगा। उस
- **Translation**: 

---

### Verse 4 (Bramha 0.8224)
- **Original**: विधिका पालन न करें तो उन्हें दोष लगता है। समय स्वधर्मनिष्ठ ब्राह्मण कोई बिरला ही होगा। यहाँतक कि भोजन और पान आदि भी उनकी एक विशेषता अवश्य है, कलियुगमें थोड़ा-सा हो
- **Translation**: 

---

### Verse 5 (Bramha 0.8225)
- **Original**: इच्छाके अनुसार नहीं प्रात होते। वे समस्त प्रयल करनेपर मनुष्य वह उत्तम पुण्यराशि प्राप्त
- **Translation**: 

---

### Verse 6 (Bramha 0.8226)
- **Original**: कार्यो्में परतन्त्र होते हैं। इस प्रकार विनीत भावसे कर सकता है, जो सत्ययुगमें बहुत बड़ी तपस्यासे
- **Translation**: 

---

### Verse 7 (Bramha 0.8227)
- **Original**: महान्‌ क्लेश उठाकर वे उत्तम लोकोंपर अधिकार ही साध्य हों सकती है। प्राप्त कत्ते हैं; परन्तु मन्त्रहीन पाक-यज्ञका अधिकारी ब्राह्णणो! कलियुग भ्रन्य है, जहाँ थोड़े ही
- **Translation**: 

---

### Verse 8 (Bramha 0.8228)
- **Original**: कृर केवल द्विजोंकी सेवा करनेमात्रसे अपने क्लेशसे महान्‌ फलकी प्राप्ति होती है तथा स्त्री
- **Translation**: 

---

### Verse 9 (Bramha 0.8229)
- **Original**: लिये अभीष्ट पुण्यलोकोंको प्राप्त कर लेता है। और शूद्र भी धन्य हैं। इसके सिवा और भी सुनो।
- **Translation**: 

---

### Verse 10 (Bramha 0.8230)
- **Original**: इसलिये शुद्र अन्य वर्णोंकी अपेक्षा अधिक धन्यवादका सत्ययुगमें दस वर्षतक तपस्या, ब्रह्मचर्य और जप
- **Translation**: 

---

### Verse 11 (Bramha 0.8231)
- **Original**: पात्र है। स्त्रियाँ क्‍यों धन्य हैं, इसका कारण आदिका अनुष्ठान करनेसे जो फल मिलता है, वह
- **Translation**: 

---

### Verse 12 (Bramha 0.8232)
- **Original**: बतलाया जाता है। पुरुषोंको अपने धर्मके त्रिपरीत त्रेतामें एक वर्ष, द्वापरमें एक मास तथा कलियुगमें
- **Translation**: 

---

### Verse 13 (Bramha 0.8233)
- **Original**: न चलकर सदा हो धनोपार्जज करना, उसे एक दिन-रातके हो अनुष्ठाससे मिल जाता है।। सुपात्रोंको देना और विधिपूर्वक यज्ञ करना आवश्यक * कस्य माता पिता कस्य यदा कर्मात्मक: पुमान्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.8234)
- **Original**: _ति चोदाहरिष्यन्ति श्वशुरानुगता नरा;
- **Translation**: 

---

### Verse 15 (Bramha 0.8235)
- **Original**: (229। 55)
- **Translation**: 

---

### Verse 16 (Bramha 0.8236)
- **Original**: धन्‍्ये कलौ भवेद्विप्रास््वल्पक्लेशैमहत्फलम्‌। तथा भवेतां स्थ्रौशुद्रो धन्यौ चान्यभ्रिबोधत
- **Translation**: 

---

### Verse 17 (Bramha 0.8237)
- **Original**: यत्कृते दशभियवर्षिस्त्रेतायां हायनेन ततू
- **Translation**: 

---

### Verse 18 (Bramha 0.8238)
- **Original**: द्वापे तच्य मासेन अहोराग्रेण तत्कलौ
- **Translation**: 

---

### Verse 19 (Bramha 0.8239)
- **Original**: तपसो ब्रह्मचर्यस्थ जपादेश्ष फल॑ द्विजाः। प्राप्रोति पुरुषस्तेन कलि: साध्विति भाषितम्‌
- **Translation**: 

---

### Verse 20 (Bramha 0.8240)
- **Original**: ध्यायन्‌ कृते यजन्‌ अज्ैस्प्रेतायां द्वापरे5र्चयनू। यदाप्तोति तदाणोति कलौ संकौर्त्य केशवम्‌
- **Translation**: 

---

