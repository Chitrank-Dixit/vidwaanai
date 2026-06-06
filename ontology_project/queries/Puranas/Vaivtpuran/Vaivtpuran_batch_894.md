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

### Verse 1 (Vaivtpuran 543.16194)
- **Original**: करो। मैं पुनः मथुरा जाऊँगा; क्योंकि मैं स्वतन्त्र जानते हैं। इस गोकुलमें आनेसे मैं धन्य हो गया।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16195)
- **Original**: नहीं हूँ; बल्कि कठपुतलीकी भाँति पराधीन हूँ यहाँ गुरुस्वरूपा गोपिकाओंसे मुझे अचल हरिभक्ति
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16196)
- **Original**: तथा जैसे बैल सदा हलवाहेके वशमें रहता है; उसी प्राप्त हुई, जिससे मैं कृतार्थ हो गया। अब मैं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16197)
- **Original**: तरह मैं श्रीकृष्णके अधीन हूँ। मथुरा नहीं जाऊँगा और प्रत्येक जन्ममें यहाँ (अध्याय 94) #0*“निस >> न उद्धवका कथन सुनकर राधाका चैतन्य होना और अपना दु:ख सुनाते हुए उद्धवको उपदेश देकर मथुरा जानेकी आज्ञा देना श्रीनारायण कहते हैं--नारद! उद्धवके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16198)
- **Original**: दुःखित हृदयसे उद्धवसे मधुर बचन बोलीं। बचन सुनकर राधिकाकौ चेतना लौट आयी। वे श्रीराधिकाने कहा--वत्स ! तुम मधुगा जाओ, उठकर उत्तम रत्नसिंहासनपर जा विराजीं। उस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16199)
- **Original**: परंतु वहाँ सुखमें पड़कर मुझे भूल मत जाना। समय सात गोपियाँ भक्तिपूर्वक श्वेत चँवरोंद्रारा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16200)
- **Original**: (यदि भूल जाओगे तो) इस भवसागरमें तुम्हारे उनकौ सेवा कर रही थीं। तब देबी राधिका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16201)
- **Original**: लिये इससे बढ़कर दूसरा अधर्म नहीं है। इस *+ धन्य भारतव्ष॑ च पुण्यद शुभद॑ चबरम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16202)
- **Original**: गोपीपादाब्जरजसा पूतं परमनिर्मलम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16203)
- **Original**: ततोषपि गोपिका धन्या मान्या योपित्सु भारते
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16204)
- **Original**: नित्य॑ पश्यन्ति राधाया: पादपच्य॑ सुपुण्यदम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16205)
- **Original**: 77-78) पल गोपीभ्यः परो भक्तो हरेश्व परमात्मन;। यादुृर्शों लेभिरे गोप्यो भक्ति तानये च तादृशीम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16206)
- **Original**: (94। 86)
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16207)
- **Original**: * श्रीकृष्णजन्मखण्ड * 707 44$$5$£ 644 4$ 4 # 4 ## 4 45 # $ 4 &# 4 6 $ # ## # 6 #£ 45 # 86 64648 # 6 ### 8 58 66 # 6 # ## # 8 55 55 5555 5 समय तुम जाकर परमानन्दस्वरूप श्रीकृष्णसे मेरी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16208)
- **Original**: सूर्य और सागर स्थगित हो जाते हैं; उन सारी बात कह सुनाओ और शीघ्र ही मेरे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16209)
- **Original**: प्रियतमको मैं किस समृद्धिको प्राप्तिसि भुला स्वामीको यहाँ ले आओ। भला, जगत्‌की युवतियोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16210)
- **Original**: सकती हूँ? भक्तवर! जो कालके काल हैं; किसको ऐसा दुःख है? श्रीकृष्णके वियोगजन्य
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16211)
- **Original**: प्रलयकालीन मेघ, संहारकर्ता शिव और सृष्टिकर्ता दुःखको मेरे अतिरिक्त और कौन जानती है ?
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16212)
- **Original**: ब्रह्माके स्वामी हैं; जो स्वाधीन, स्वतन्त्र और स्वयं सीताकों भी वियोग-दुःख कुछ-कुछ ज्ञात है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16213)
- **Original**: ही आत्मा नामवाले हैं; उन प्रभुको मैं कौन-सी त्रिलोकीमें नारियोंमें मुझसे बढ़कर दुःख्िया कोई
- **Translation**: 

---

