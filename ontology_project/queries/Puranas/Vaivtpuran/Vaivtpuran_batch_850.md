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

### Verse 1 (Vaivtpuran 543.15314)
- **Original**: निश्चित है। जो भस्म और अद्भास्युक्त गड्ढोंमें, जटाधारी, सूअर, भेंसा, गदहा, महाघोर अन्धकार,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15315)
- **Original**: क्षारकुण्डोंमें तथा धूलिकी राशिपर ऊँचाईसे गिरते मरा हुआ भयंकर जीव और योनि-चिह्न देखकर हैं; निस्संदेह उनकी मृत्यु होती है। जिसके मनुष्य निश्चय ही विपत्तिमें फँस जाता है। कुवेषधारी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15316)
- **Original**: मस्तकपरसे कोई दुष्ट बलपूर्वक छत्र खींच लेता म्लेच्छ और पाश ही जिसका शस्त्र है, ऐसे है; उसके पिता, गुरु अथवा राजाका नाश हो पाशधारी भयंकर यमदूतकों देखकर मनुष्य मृत्युको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15317)
- **Original**: जाता है। जिसके घरसे भयभीत हुई गौ बछड़ेसहित प्राप्त हो जाता है। ब्राह्मण, ब्राह्मणी, छोटी कन्या
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15318)
- **Original**: चली जाती है; उस पापीकी लक्ष्मी और पृथ्वी भी और बालक-पुत्र क्रोधवश विलाप करते हों तो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15319)
- **Original**: नष्ट हो जाती है। म्लेच्छ यमदूत जिसे पाशसे उन्हें देखकर दुःखको प्राप्ति होती है। काला फूल,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15320)
- **Original**: बाँधकर ले जाते हैं; उसकी मृत्यु निश्चित है। जिसे काले फूलोंकी माला, श्त्रास्त्रधारो सेना और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15321)
- **Original**: ज्योतिषी ब्राह्मण, ब्राह्मणी तथा गुरु रुष्ट होकर बिकृत आकारवाली म्लेच्छवर्णकी स्त्रीको देखनेसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15322)
- **Original**: शाप देते हैं; उसे निश्चय ही विपत्ति भोगनी पड़ती निस्संदेह मृत्यु गले लग जाती है। बाजा, नाच,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15323)
- **Original**: है। जिसके शरीरपर शत्रुदल, कौए, मुर्गें और रीछ गान, गबैया, लाल वस्त्र, बजाया जाता हुआ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15324)
- **Original**: आकर टूट पड़ते हैं; उसकी अवश्य मृत्यु हो मृदड्ग--इन्हें देखकर अवश्यमेव दुःख मिलता है।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15325)
- **Original**: जाती है और स्वप्रमें जिसके ऊपर भैंसे, भालू, प्राणशहित (मुर्दे)-को देखकर निश्चय ही मृत्यु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15326)
- **Original**: ऊँट, सूअर और गदहे क्रुद्ध होकर धावा करते हैं; होती है और जो मत्स्य आदिको धारण करता है,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15327)
- **Original**: वह निश्चय ही रोगी हो जाता है। उसके भाईका मरण ध्रुव है। घायल अथबा बिना जो लाल चन्दनकी लकड़ीको घीमें डुबोकर सिरका धड़ अथवा मुण्डित सिरवाले एवं शीघ्रतापूर्वक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15328)
- **Original**: एक सहस््र गायत्री-मन्त्रद्वारा अग्निमें हवन करता नाचते हुए बेडौल प्राणीकों देखकर मनुष्य मौतका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15329)
- **Original**: है; उसका दुःस्वप्रजनित दोष शान्त हो जाता है। भागी हो जाता है। मरा हुआ पुरुष अथवा मरी जो भक्तिपूर्वक इन मधुसूदनका एक हजार जप
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15330)
- **Original**: 666 + संक्षिप्त ब्रह्मवैयर्तपुराण + करता है; बह निष्पाप हो जाता है और उसका दुःस्वप्न भी सुखदायक हो जाता है। जो विद्वान्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15331)
- **Original**: शुभदायक हो जाता है। “3 हीं श्रीं क्लीं दुर्गतिनाशिन्ये महामायायै स्वाहा '-- यह सप्तदशाक्षर- पवित्र हो पूर्वकी ओर मुख करके अच्युत, केशव,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15332)
- **Original**: मन्त्र लोगोंके लिये कल्पवृक्षके समान है। इसका विष्णु, हरि, सत्य, जनार्दन, हंस, नारायण-इन आठ शुभ नामोंका दस बार जप्र करता है, उसका पाप नष्ट हो जाता है तथा दुःस्वप्र भी शुभकारक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15333)
- **Original**: हो जाता है। जो भक्त भक्तिपूर्वक विष्णु, नारायण, कृष्ण, माधव, मधुसूदन, हरि, नरहारि, राम,
- **Translation**: 

---

