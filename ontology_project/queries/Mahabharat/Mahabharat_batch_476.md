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

### Verse 1 (Mahabharat 0.4751)
- **Original**: गिराया और सौ बाणोंसे श्रीकृष्णको तथा तीन सौसे दिव्याखका प्रयोग किया, किंतु अश्वश्ामाने उसका
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4751)
- **Original**: गिराया और सौ बाणोंसे श्रीकृष्णको तथा तीन सौसे दिव्याखका प्रयोग किया, किंतु अश्वश्ामाने उसका
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4752)
- **Original**: अर्जुनको बींध डाल्पम। तब अर्जुनने भी अश्वस्थापाके निवारण कर दिया। उस समय अर्जुनने अश्वश्षामाका वध
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4752)
- **Original**: अर्जुनको बींध डाल्पम। तब अर्जुनने भी अश्वस्थापाके निवारण कर दिया। उस समय अर्जुनने अश्वश्षामाका वध
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4753)
- **Original**: मर्मस्थानोंमें साँ बाण मारे और उस्तके सारधिको एक कसनेके लिये जिस-जिस अखका प्रहार किया, उन सबको
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4753)
- **Original**: मर्मस्थानोंमें साँ बाण मारे और उस्तके सारधिको एक कसनेके लिये जिस-जिस अखका प्रहार किया, उन सबको
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4754)
- **Original**: भल्लसे मास्कर श्रेणकुमारने काट डाला । उसने अपने बांणोंसे दिशाओं तथा
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4754)
- **Original**: भल्लसे मास्कर श्रेणकुमारने काट डाला । उसने अपने बांणोंसे दिशाओं तथा
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4755)
- **Original**: अश्वत्थामाने स्वयं उपदिशञाओंकों ढककर श्रीकृष्णकी दाहिनी बाँहमें तीन बाण
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4755)
- **Original**: अश्वत्थामाने स्वयं उपदिशञाओंकों ढककर श्रीकृष्णकी दाहिनी बाँहमें तीन बाण
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4756)
- **Original**: श्रीकृष्ण तथां अर्जुनकों बाणोंसे ढकता आरम्भ किया। मारे। तब अ्जुनने उसके घोड़ोंकों घायल करके संग्राममें
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4756)
- **Original**: श्रीकृष्ण तथां अर्जुनकों बाणोंसे ढकता आरम्भ किया। मारे। तब अ्जुनने उसके घोड़ोंकों घायल करके संग्राममें
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4757)
- **Original**: उसके खूनकी नदी बहा दी। उन्होंने अश्नत्यामाका धनुष काट
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4757)
- **Original**: उसके खूनकी नदी बहा दी। उन्होंने अश्नत्यामाका धनुष काट
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4758)
- **Original**: बींचमें न डाला। यह देख उसने अर्जुनपर बज्रके समान भयंकर
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4758)
- **Original**: बींचमें न डाला। यह देख उसने अर्जुनपर बज्रके समान भयंकर
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4759)
- **Original**: क्षुओंसे तुरंत काट डाला। अब वे घोड़े बाणोंकी मारसे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4759)
- **Original**: क्षुओंसे तुरंत काट डाला। अब वे घोड़े बाणोंकी मारसे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4760)
- **Original**: कर्णपर्व अश्ठत्थामाकी पराजय, कर्णड्वारा भार्गवासूत्का प्रयोग और युधिष्ठिस्का अर्जुससे प्रश्न 7 अत्वच्त पीड़ित होकर भाग चले। उस समय पाण्छव
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4760)
- **Original**: कर्णपर्व अश्ठत्थामाकी पराजय, कर्णड्वारा भार्गवासूत्का प्रयोग और युधिष्ठिस्का अर्जुससे प्रश्न 7 अत्वच्त पीड़ित होकर भाग चले। उस समय पाण्छव
- **Translation**: 

---

