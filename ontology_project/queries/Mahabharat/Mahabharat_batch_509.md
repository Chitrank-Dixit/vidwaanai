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

### Verse 1 (Mahabharat 0.5081)
- **Original**: सहल्नों गौओंका दान तथा कितने ही क्षत्रिय-जीरोंका संहार
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5081)
- **Original**: सहल्नों गौओंका दान तथा कितने ही क्षत्रिय-जीरोंका संहार
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5082)
- **Original**: किया है। भीमसेत ! उस समय जब कि प्रधान-प्रधान
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5082)
- **Original**: किया है। भीमसेत ! उस समय जब कि प्रधान-प्रधान
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5083)
- **Original**: 'ई (का हा
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5083)
- **Original**: 'ई (का हा
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5084)
- **Original**: गरम-गरम रक्त पीने लूगे। तदनन्तर, उन्होंने ललबार उठायी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5084)
- **Original**: गरम-गरम रक्त पीने लूगे। तदनन्तर, उन्होंने ललबार उठायी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5085)
- **Original**: और उसप्तका मस्तक घड़से अलग कर दिया। इस प्रकार
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5085)
- **Original**: और उसप्तका मस्तक घड़से अलग कर दिया। इस प्रकार
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5086)
- **Original**: गरम-गरम रक्त-पान किया। वे उसका स्वाद लेकर कहने हूगे--'मैंने माताके दूधका, शहद और घीका तथा दिल्य रसका भी आस्वादन किया है, दूध और दहीसे बिल्ओोये हुए
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5086)
- **Original**: गरम-गरम रक्त-पान किया। वे उसका स्वाद लेकर कहने हूगे--'मैंने माताके दूधका, शहद और घीका तथा दिल्य रसका भी आस्वादन किया है, दूध और दहीसे बिल्ओोये हुए
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5087)
- **Original**: वाजे माखनका भी स्वाद लिया हैं। इनके अल्लावे भी संसारमें बहुत-से पान करनेयोग्य पदार्थ हैं, जिनमें अमृ्तके समान मधुर स्वाद है; परेंतु मेरें शत्रुके इस रक्तका स्वाद तो उन सबसे विलक्षण है, इसमें सबसे अधिक रस है !” यों कहकर वे बारंबार उसके रक्तका आस्वादन करते
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5087)
- **Original**: वाजे माखनका भी स्वाद लिया हैं। इनके अल्लावे भी संसारमें बहुत-से पान करनेयोग्य पदार्थ हैं, जिनमें अमृ्तके समान मधुर स्वाद है; परेंतु मेरें शत्रुके इस रक्तका स्वाद तो उन सबसे विलक्षण है, इसमें सबसे अधिक रस है !” यों कहकर वे बारंबार उसके रक्तका आस्वादन करते
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5088)
- **Original**: कर्णपर्व ] और अत्यन्त हर्षमें भरकर उछलने-कूदने छूगते थे । उस समय जिन्होंने उनकी ओर देखा, बे भयसे व्याकुल हो पृथ्वीपर गिर पड़े। जो घबराये नहीं, उनके हाथोंसे भी हथियार तो गिर ही पड़ा। कितने हो भयके मारे आँखें बंद करके चौंखने-चिल्लाने छगे। रक्त पीते समय उनका रूप बड़ा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5088)
- **Original**: कर्णपर्व ] और अत्यन्त हर्षमें भरकर उछलने-कूदने छूगते थे । उस समय जिन्होंने उनकी ओर देखा, बे भयसे व्याकुल हो पृथ्वीपर गिर पड़े। जो घबराये नहीं, उनके हाथोंसे भी हथियार तो गिर ही पड़ा। कितने हो भयके मारे आँखें बंद करके चौंखने-चिल्लाने छगे। रक्त पीते समय उनका रूप बड़ा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5089)
- **Original**: भर्येकर जान पड़ता था। उस समय बहुत-से योद्धा भयभीत
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5089)
- **Original**: भर्येकर जान पड़ता था। उस समय बहुत-से योद्धा भयभीत
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5090)
- **Original**: होकर “अरे ! यह मनुष्य नहीं राक्षस है' ऐसा कहते हुए चित्रस्तेनके साथ भागने छगे। चित्रसेनको भागते देख युधामन्युने अपनी सेनाके साथ उसका पीछा किया और तेज किये हुए सात बाण मारकर उसे बींध डाला । चित्रसेनने भी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5090)
- **Original**: होकर “अरे ! यह मनुष्य नहीं राक्षस है' ऐसा कहते हुए चित्रस्तेनके साथ भागने छगे। चित्रसेनको भागते देख युधामन्युने अपनी सेनाके साथ उसका पीछा किया और तेज किये हुए सात बाण मारकर उसे बींध डाला । चित्रसेनने भी
- **Translation**: 

---

