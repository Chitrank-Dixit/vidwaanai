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

### Verse 1 (Mahabharat 0.5051)
- **Original**: संप्राममें मैं तेरा रक्त-पान करूँगा।'
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5051)
- **Original**: संप्राममें मैं तेरा रक्त-पान करूँगा।'
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5052)
- **Original**: भीमके ऐसा कहते ही दुःझासनने उनके ऊपर एक
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5052)
- **Original**: भीमके ऐसा कहते ही दुःझासनने उनके ऊपर एक
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5053)
- **Original**: भर्येकर झक्ति चल्तायी, इधस्से भीमतने भी अपनी भयानक गदा घुमाकर फेंकी। वह गदा दुः/शासनकी झक्तिकों
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5053)
- **Original**: भर्येकर झक्ति चल्तायी, इधस्से भीमतने भी अपनी भयानक गदा घुमाकर फेंकी। वह गदा दुः/शासनकी झक्तिकों
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5054)
- **Original**: दक-दूक करती हुईं उसके मस्तकमें जा लगी। गदाके
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5054)
- **Original**: दक-दूक करती हुईं उसके मस्तकमें जा लगी। गदाके
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5055)
- **Original**: आघालसे दुःझासनका रथ दस धनुष पीछे हट गया। उसके
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5055)
- **Original**: आघालसे दुःझासनका रथ दस धनुष पीछे हट गया। उसके
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5056)
- **Original**: झरीरपर भी बहुत सख्त चोट पहुँची थी, कवच टूट गया,
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5056)
- **Original**: झरीरपर भी बहुत सख्त चोट पहुँची थी, कवच टूट गया,
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5057)
- **Original**: आभूषण और हार बिखर गये, कपड़े फट गये तथा वह <आ 0 924 हः
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5057)
- **Original**: आभूषण और हार बिखर गये, कपड़े फट गये तथा वह <आ 0 924 हः
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5058)
- **Original**: जमीनपर गिर पड़ा। इतना ही नहीं, उस गदासे दुःझासनके कक 30 %/ “6 2//7/वप. घोड़े घारे गये और उसके रथकी भी धजियाँ उड़ गयी। 2, 50 6/2/ .2 / ककाकती हा अगक के शशीरियकक बह घाव किया और दूसरेसे उसके सारथ्िका मस्तक भी घड़से
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5058)
- **Original**: जमीनपर गिर पड़ा। इतना ही नहीं, उस गदासे दुःझासनके कक 30 %/ “6 2//7/वप. घोड़े घारे गये और उसके रथकी भी धजियाँ उड़ गयी। 2, 50 6/2/ .2 / ककाकती हा अगक के शशीरियकक बह घाव किया और दूसरेसे उसके सारथ्िका मस्तक भी घड़से
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5059)
- **Original**: अल्वत्त प्रसन्न होकर सिंहनाद करने लगे। भीमको बारह ब्राणोंसे बंध डाल्म और स्वयं ही घोड़ोंको
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5059)
- **Original**: अल्वत्त प्रसन्न होकर सिंहनाद करने लगे। भीमको बारह ब्राणोंसे बंध डाल्म और स्वयं ही घोड़ोंको
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5060)
- **Original**: गये और सम्पूर्ण दिज्ञाओंको ग्रतिध्यनित करते हुए कामयूमें रखते हुए उसने पुन: उनके ऊपर बाणोंकी झड़ी लूगा
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5060)
- **Original**: गये और सम्पूर्ण दिज्ञाओंको ग्रतिध्यनित करते हुए कामयूमें रखते हुए उसने पुन: उनके ऊपर बाणोंकी झड़ी लूगा
- **Translation**: 

---

